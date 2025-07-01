from django.shortcuts import render
import requests
from observations.models import Observation
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import os
from dotenv import load_dotenv

load_dotenv()

# Create your views here.
def splash(request):
    return render(request,'home/splash.html')

def home_view(request):
        logs = Observation.objects.all().order_by('-created_at')[:10]
        return render(request, 'home/home.html', {'logs': logs, 'nasa_api_key': os.getenv('NASA_API_KEY')})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
