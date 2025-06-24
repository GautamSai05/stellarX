from django.shortcuts import render
from observations.models import Observation
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
def splash(request):
    return render(request,'home/splash.html')

def home_view(request):
        logs = Observation.objects.all().order_by('-created_at')[:10]
        apod = {}
        try:
            r = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
            if r.status_code == 200:
                apod = r.json()
        except:
            pass
        return render(request, 'home/home.html', {'logs': logs, 'apod': apod})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
