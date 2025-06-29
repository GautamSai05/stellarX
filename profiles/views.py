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

    # Daily log counts for the line chart
    daily_log_data = []
    max_log_count_day = 0
    
    start_date = date(selected_year, 1, 1)
    end_date = date(selected_year, 12, 31)
    
    current_date = start_date
    while current_date <= end_date:
        count = Observation.objects.filter(
            user=user,
            created_at__date=current_date
        ).count()
        daily_log_data.append({
            'date': current_date,
            'count': count
        })
        if count > max_log_count_day:
            max_log_count_day = count
        current_date += timedelta(days=1)

    # Prepare data for SVG line chart
    chart_width = 900
    chart_height = 180 # Height of the actual chart area
    x_offset = 50 # Padding for Y-axis labels
    y_offset = 180 # Y-coordinate for the X-axis line

    # Calculate derived coordinates for template
    x_axis_line_x2 = chart_width + x_offset
    y_axis_line_x2 = chart_width + x_offset
    x_axis_label_x = chart_width / 2 + x_offset

    points = []
    for i, data in enumerate(daily_log_data):
        x_pos = x_offset + (i / len(daily_log_data) * chart_width)
        y_pos = y_offset - (data['count'] / (max_log_count_day if max_log_count_day > 0 else 1) * chart_height)
        points.append(f"{x_pos},{y_pos}")
    points_string = " ".join(points)

    # Y-axis ticks
    y_axis_ticks = []
    num_y_ticks = 5
    for i in range(num_y_ticks):
        tick_value = round(max_log_count_day / (num_y_ticks - 1) * i)
        tick_y_pos = y_offset - (tick_value / (max_log_count_day if max_log_count_day > 0 else 1) * chart_height)
        y_axis_ticks.append({'value': tick_value, 'y_pos': tick_y_pos})

    return render(request, 'profiles/profile.html', {
        'user': user, 
        'logs': logs, 
        'years': years, 
        'selected_year': selected_year,
        'daily_log_data': daily_log_data,
        'max_log_count_day': max_log_count_day,
        'start_date': start_date,
        'end_date': end_date,
        'points_string': points_string,
        'y_axis_ticks': y_axis_ticks,
        'chart_width': chart_width,
        'chart_height': chart_height,
        'x_offset': x_offset,
        'y_offset': y_offset,
        'x_axis_line_x2': x_axis_line_x2,
        'y_axis_line_x2': y_axis_line_x2,
        'x_axis_label_x': x_axis_label_x,
    })
