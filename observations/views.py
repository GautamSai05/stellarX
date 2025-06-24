from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from .models import Observation
from .forms import ObservationForm
from django.contrib.auth.decorators import login_required

@login_required
def log_create(request):
    if request.method == 'POST':
        form = ObservationForm(request.POST, request.FILES)
        if form.is_valid():
            log = form.save(commit=False)
            log.user = request.user
            log.save()
            return redirect('home')
    else:
        form = ObservationForm()
    return render(request, 'observations/log_form.html', {'form': form})

def log_list(request):
    logs = Observation.objects.all().order_by('-created_at')
    return render(request, 'home/home.html', {'logs': logs})
