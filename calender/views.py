import os
from django.shortcuts import render
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

def calendar_chatbot(request):
    return render(request, 'calender/calender.html', {
        'GEMINI_API_KEY': os.getenv('GEMINI_API_KEY')
    })
