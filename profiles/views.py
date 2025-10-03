from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from observations.models import Observation

def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    logs = Observation.objects.filter(user=user).order_by('-created_at')

    return render(request, 'profiles/profile.html', {
        'user': user, 
        'logs': logs, 
    })
