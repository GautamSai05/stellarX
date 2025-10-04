import os
import requests
from django.shortcuts import render
from dotenv import load_dotenv
from .models import AstronomicalEvent
from django.http import JsonResponse

# Load .env variables
load_dotenv()

# n8n webhook URL
N8N_WEBHOOK_URL = "https://sample18102.app.n8n.cloud/webhook/6a7a1a2f-2d23-4780-bb5a-9b38413507b3/chat"

def query_n8n_webhook(message, session_id="calendar_chat"):
    """
    Query the n8n webhook and return the response
    """
    try:
        payload = {
            "chatInput": message,
            "sessionId": session_id
        }
        
        response = requests.post(
            N8N_WEBHOOK_URL,
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            # Extract the response text from n8n webhook
            if isinstance(data, dict):
                # n8n typically returns the response in different formats
                # Try common response patterns
                return data.get('output', data.get('text', data.get('response', str(data))))
            return str(data)
        else:
            return f"❌ n8n webhook returned status code: {response.status_code}"
            
    except requests.Timeout:
        return "❌ Request to n8n webhook timed out. Please try again."
    except Exception as e:
        return f"❌ Error connecting to n8n webhook: {str(e)}"

def calendar_chatbot(request):
    if request.method == 'POST':
        user_message = request.POST.get("date", "").strip()
        if not user_message:
            return JsonResponse({"description": "❌ Please enter a message."})

        # Route all queries to n8n webhook
        session_id = request.session.session_key or "calendar_chat"
        reply = query_n8n_webhook(user_message, session_id)
        return JsonResponse({"description": reply})

    return render(request, 'calender/calender.html')
