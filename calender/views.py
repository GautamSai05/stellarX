import os
from django.shortcuts import render
from dotenv import load_dotenv
from .models import AstronomicalEvent
from django.http import JsonResponse
from dateutil.parser import parse, ParserError
import google.generativeai as genai

# Load .env variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
gemini_model = genai.GenerativeModel("models/gemini-1.5-flash")

def calendar_chatbot(request):
    if request.method == 'POST':
        user_date = request.POST.get("date", "").strip()
        if not user_date:
            return JsonResponse({"description": "❌ Please enter a date."})

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
