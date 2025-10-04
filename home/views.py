from django.shortcuts import render
import requests
from observations.models import Observation
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
import os
from dotenv import load_dotenv
from datetime import date
from calender.models import AstronomicalEvent

load_dotenv()

def stellarium(request):
    return render(request, 'home/stellarium.html')

# Create your views here.
def splash(request):
    return render(request,'home/splash.html')

def home_view(request):
        logs = Observation.objects.all().order_by('-created_at')[:10]
        today_events = AstronomicalEvent.objects.filter(date=date.today())
        return render(request, 'home/home.html', {'logs': logs, 'nasa_api_key': os.getenv('NASA_API_KEY'), 'today_events': today_events})

def timeline(request):
    """Render the interactive space timeline page."""
    return render(request, 'home/timeline.html')

def calculator(request):
    """Render the astronomical calculator tools page."""
    return render(request, 'home/calculator.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'You have been successfully registered! Please log in.')
            return redirect(f"{reverse('login')}?username={user.username}")
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
