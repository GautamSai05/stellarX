"""
Context processor to provide active solar alerts to all templates
"""
from django.utils import timezone
from .models import SolarAlert


def active_alerts(request):
    """
    Add active solar alerts to the template context.
    Filters alerts based on user's profile preferences.
    """
    context = {'active_alerts': []}
    
    if not request.user.is_authenticated:
        return context
    
    # Get user's profile
    if not hasattr(request.user, 'profile'):
        return context
    
    profile = request.user.profile
    
    # Only show alerts if user has opted in
    if not profile.receive_alerts:
        return context
    
    # Get active alerts
    alerts = SolarAlert.objects.filter(
        is_active=True,
        detected_at__gte=timezone.now() - timezone.timedelta(days=7)
    )
    
    # Filter alerts based on user's profession
    profession = profile.profession
    filtered_alerts = []
    
    for alert in alerts:
        if profession == 'farmer' and alert.relevant_for_farmers:
            filtered_alerts.append({
                'alert': alert,
                'message': alert.get_targeted_message('farmer'),
                'color': 'yellow'
            })
        elif profession == 'pilot' and alert.relevant_for_pilots:
            filtered_alerts.append({
                'alert': alert,
                'message': alert.get_targeted_message('pilot'),
                'color': 'red'
            })
        elif profession == 'stargazer' and alert.relevant_for_stargazers:
            filtered_alerts.append({
                'alert': alert,
                'message': alert.get_targeted_message('stargazer'),
                'color': 'purple'
            })
        elif profession == 'educator' and alert.relevant_for_educators:
            filtered_alerts.append({
                'alert': alert,
                'message': alert.get_targeted_message('educator'),
                'color': 'blue'
            })
        elif profession == 'general' and alert.relevant_for_general:
            filtered_alerts.append({
                'alert': alert,
                'message': alert.get_targeted_message('general'),
                'color': 'blue'
            })
    
    # Limit to most recent 3 alerts
    context['active_alerts'] = filtered_alerts[:3]
    
    return context
