from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from observations.models import Observation
from datetime import date, timedelta
from collections import Counter

def profile_view(request, username, year=None):
    user = get_object_or_404(User, username=username)
    logs = Observation.objects.filter(user=user).order_by('-created_at')

    # Year selection
    today = date.today()
    selected_year = year if year else today.year
    first_log = Observation.objects.filter(user=user).order_by('created_at').first()
    first_year = first_log.created_at.year if first_log else today.year
    years = range(first_year, today.year + 1)

    # Monthly log counts for the bar chart
    monthly_log_data = []
    max_log_count_month = 0
    for month_num in range(1, 13):
        count = Observation.objects.filter(
            user=user,
            created_at__year=selected_year,
            created_at__month=month_num
        ).count()
        monthly_log_data.append({
            'month_num': month_num,
            'count': count
        })
        if count > max_log_count_month:
            max_log_count_month = count

    # Calculate bar heights based on max_log_count_month
    for item in monthly_log_data:
        item['bar_height'] = (item['count'] / max_log_count_month * 100) if max_log_count_month > 0 else 0

    return render(request, 'profiles/profile.html', {
        'user': user, 
        'logs': logs, 
        'years': years, 
        'selected_year': selected_year,
        'monthly_log_data': monthly_log_data,
    })
