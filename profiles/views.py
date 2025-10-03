from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from observations.models import Observation
from .models import UserProfile
from .forms import UserProfileForm

def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    logs = Observation.objects.filter(user=user).order_by('-created_at')
    
    # Ensure the user has a profile
    profile, created = UserProfile.objects.get_or_create(user=user)

    return render(request, 'profiles/profile.html', {
        'user': user, 
        'logs': logs,
        'profile': profile,
    })

@login_required
def profile_settings_view(request):
    """View for updating user profile settings"""
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile settings have been updated successfully!')
            return redirect('profile', username=request.user.username)
    else:
        form = UserProfileForm(instance=profile)
    
    return render(request, 'profiles/settings.html', {
        'form': form,
        'profile': profile,
    })
