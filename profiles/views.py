from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from observations.models import Observation
from .models import UserProfile

def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    logs = Observation.objects.filter(user=user).order_by('-created_at')

    # Own profile settings update
    if request.user.is_authenticated and request.user == user and request.method == 'POST':
        profession = request.POST.get('profession', '').strip()
        alert_opt_in = True if request.POST.get('alert_opt_in') == 'on' else False

        profile, _ = UserProfile.objects.get_or_create(user=user)
        profile.profession = profession
        profile.alert_opt_in = alert_opt_in
        profile.save()
        messages.success(request, 'Profile settings updated.')
        return redirect('profile', username=user.username)

    # Ensure profile exists for display
    profile, _ = UserProfile.objects.get_or_create(user=user)

    return render(request, 'profiles/profile.html', {
        'user': user,
        'logs': logs,
        'profile': profile,
    })
