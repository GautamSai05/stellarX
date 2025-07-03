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
        prompt = f"Describe any astronomical phenomena or events visible from Earth on {user_date}, even minor ones. If nothing significant, state that. Be concise and informative."
        try:
            response = gemini_model.generate_content(prompt)
            reply = response.text.strip() if response.text else "No information available from Gemini API."
            return JsonResponse({"description": reply})
        except Exception as e:
            return JsonResponse({"description": f"❌ Gemini API Error: {e}"})

    return render(request, 'calender/calender.html', {
        'GEMINI_API_KEY': os.getenv('GEMINI_API_KEY')  # optional
    })
