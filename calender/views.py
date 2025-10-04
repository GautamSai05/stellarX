import os
import requests
import re
from django.shortcuts import render
from dotenv import load_dotenv
from .models import AstronomicalEvent
from django.http import JsonResponse, StreamingHttpResponse
from dateutil.parser import parse, ParserError
import google.generativeai as genai
import json

# Load .env variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
gemini_model = genai.GenerativeModel("models/gemini-2.5-flash")

# n8n webhook URL
N8N_WEBHOOK_URL = "https://sample18102.app.n8n.cloud/webhook/6a7a1a2f-2d23-4780-bb5a-9b38413507b3/chat"

def is_astrology_query(user_input):
    """
    Detect if the user's query is related to astrology/space weather topics
    based on the n8n workflow's system message context
    """
    astrology_keywords = [
        'solar flare', 'aurora', 'cosmic', 'space weather', 'earthlings',
        'solar wind', 'magnetic storm', 'coronal mass ejection', 'cme',
        'geomagnetic', 'ionosphere', 'magnetosphere', 'solar storm',
        'radiation belt', 'cosmic ray', 'solar activity', 'sun spot',
        'northern lights', 'southern lights', 'solar radiation',
        'space environment', 'heliosphere', 'solar cycle', 'solar maximum',
        'solar minimum', 'solar particle', 'astrology', 'horoscope',
        'zodiac', 'constellation', 'planetary alignment', 'celestial influence'
    ]
    
    user_input_lower = user_input.lower()
    
    # Check if any astrology-related keyword is present
    for keyword in astrology_keywords:
        if keyword in user_input_lower:
            return True
    
    return False

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

        # Check if this is an astrology-related query
        if is_astrology_query(user_message):
            # Route to n8n webhook for astrology queries
            session_id = request.session.session_key or "calendar_chat"
            reply = query_n8n_webhook(user_message, session_id)
            return JsonResponse({
                "description": reply,
                "source": "n8n"
            })
        
        # Try to parse as a date for historical astronomical events
        try:
            parsed_date = parse(user_message).date()
            is_date = True
        except (ParserError, ValueError):
            is_date = False

        if is_date:
            # Query Gemini API for historical astronomical events on this date
            prompt = f"Search for notable astronomical, astrophysical, or space-related historical events that occurred on {user_message}, ignoring the year. These can include celestial discoveries, spacecraft launches, astronaut milestones, telescope deployments, or landmark scientific findings. Present each event as a short, engaging story suitable for astronomy enthusiasts visiting a homepage. Be educational, accurate, and use a touch of creativity. If nothing important happened, state it clearly but positively."
        else:
            # General astronomy query - use Gemini
            prompt = user_message
        
        try:
            response = gemini_model.generate_content(prompt)
            reply = response.text.strip() if response.text else "No information available from Gemini API."
            return JsonResponse({
                "description": reply,
                "source": "gemini"
            })
        except Exception as e:
            return JsonResponse({"description": f"❌ Gemini API Error: {e}"})

    return render(request, 'calender/calender.html', {
        'GEMINI_API_KEY': os.getenv('GEMINI_API_KEY')  # optional
    })
