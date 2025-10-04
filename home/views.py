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
    # Home page now shows hero/preview and APOD only; feeds moved to their own page
    return render(request, 'home/home.html', {'nasa_api_key': os.getenv('NASA_API_KEY')})

def feeds(request):
    """Render the Feeds page containing today's events and recent logs."""
    username = request.GET.get('user') or request.GET.get('username')
    if username:
        logs = Observation.objects.filter(user__username=username).order_by('-created_at')[:50]
    else:
        logs = Observation.objects.all().order_by('-created_at')[:50]
    today_events = AstronomicalEvent.objects.filter(date=date.today())
    return render(request, 'home/feeds.html', {'logs': logs, 'today_events': today_events})

def timeline(request):
    """Render the interactive space timeline page."""
    return render(request, 'home/timeline.html')

def calculator(request):
    """Render the astronomical calculator tools page."""
    return render(request, 'home/calculator.html')

def museum(request):
    """Render the virtual space museum page."""
    return render(request, 'home/museum.html')

def starmap(request):
    """Render the interactive star map page."""
    return render(request, 'home/starmap.html')

def videogallery(request):
    """Render the video gallery page."""
    return render(request, 'home/videogallery.html')

def photogallery(request):
    """Render the photo gallery page."""
    return render(request, 'home/photogallery.html')

def whatif(request):
    """Render the What-If Simulator page."""
    return render(request, 'home/whatif.html')

def women_in_space(request):
    """Render the Women in Space spotlight page."""
    return render(request, 'home/women_in_space.html')

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
