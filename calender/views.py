import os
from django.shortcuts import render
import requests
from dotenv import load_dotenv
from .models import AstronomicalEvent
from django.http import JsonResponse
from dateutil.parser import parse, ParserError
import google.generativeai as genai

# Load .env variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
gemini_model = genai.GenerativeModel("models/gemini-2.5-flash")

N8N_CHAT_WEBHOOK_URL = "https://sample18102.app.n8n.cloud/webhook/6a7a1a2f-2d23-4780-bb5a-9b38413507b3/chat"

def calendar_chatbot(request):
    if request.method == 'POST':
        # Astrology/freeform chat routed to n8n when a free-text message is provided
        user_message = request.POST.get("message", "").strip()
        if user_message:
            try:
                n8n_response = requests.post(
                    N8N_CHAT_WEBHOOK_URL,
                    json={"message": user_message},
                    timeout=20,
                )

                reply_text = None
                # Try to extract a useful reply from JSON; fall back to raw text
                try:
                    payload = n8n_response.json()
                    if isinstance(payload, dict):
                        if isinstance(payload.get("reply"), str):
                            reply_text = payload["reply"]
                        elif isinstance(payload.get("text"), str):
                            reply_text = payload["text"]
                        elif isinstance(payload.get("message"), str):
                            reply_text = payload["message"]
                        elif isinstance(payload.get("data"), dict):
                            data_obj = payload["data"]
                            for key in ("reply", "text", "message", "content"):
                                if isinstance(data_obj.get(key), str):
                                    reply_text = data_obj[key]
                                    break
                        elif isinstance(payload.get("messages"), list):
                            messages = payload["messages"]
                            for msg in reversed(messages):
                                if isinstance(msg, dict):
                                    for key in ("message", "text", "content"):
                                        val = msg.get(key)
                                        if isinstance(val, str) and val.strip():
                                            reply_text = val
                                            break
                                    if reply_text:
                                        break
                    if not reply_text:
                        reply_text = n8n_response.text
                except ValueError:
                    reply_text = n8n_response.text

                return JsonResponse({"description": reply_text})
            except Exception as e:
                return JsonResponse({"description": f"❌ n8n Error: {e}"})

        # Date-based queries handled locally via Gemini
        user_date = request.POST.get("date", "").strip()
        if not user_date:
            return JsonResponse({"description": "❌ Please enter a date or message."})

        try:
            parsed_date = parse(user_date).date()
        except (ParserError, ValueError):
            return JsonResponse({"description": "❌ Invalid date format."})

        # Always query Gemini API for the event description
        prompt =  f"Search for notable astronomical, astrophysical, or space-related historical events that occurred on {user_date}, ignoring the year. These can include celestial discoveries, spacecraft launches, astronaut milestones, telescope deployments, or landmark scientific findings. Present each event as a short, engaging story suitable for astronomy enthusiasts visiting a homepage. Be educational, accurate, and use a touch of creativity. If nothing important happened, state it clearly but positively."
        try:
            response = gemini_model.generate_content(prompt)
            reply = response.text.strip() if response.text else "No information available from Gemini API."
            return JsonResponse({"description": reply})
        except Exception as e:
            return JsonResponse({"description": f"❌ Gemini API Error: {e}"})

    return render(request, 'calender/calender.html', {
        'GEMINI_API_KEY': os.getenv('GEMINI_API_KEY')  # optional
    })
