# Space Weather Alert System

## Overview

The StellarSense platform now includes a comprehensive Space Weather Alert System that delivers targeted, real-time alerts to users based on their interests or profession. This system monitors data from NOAA's Space Weather Prediction Center (SWPC) and provides customized notifications for different user groups.

## Features

### 1. User Profile Enhancements

Users can now specify their interest or profession in their profile settings:

- **Stargazer**: Interested in aurora viewing and celestial phenomena
- **Farmer**: Using precision agriculture equipment (GPS-dependent)
- **Pilot**: Aviation professionals concerned about radio communications
- **Educator**: Teachers looking for educational opportunities
- **General Interest**: Anyone interested in space weather

### 2. Targeted Alert System

Based on user preferences, the system delivers customized alerts:

#### For Farmers 🚜
- GPS disruption warnings during solar flares
- Radio blackout notifications affecting precision agriculture
- Example: *"HEADS UP: A recent M-class solar flare may cause GPS inaccuracies for the next 24-48 hours."*

#### For Pilots ✈️
- Radio blackout alerts (R2-R5 events)
- Solar radiation storm warnings
- HF communication degradation notices
- Example: *"AVIATION ALERT: An R3 (Strong) radio blackout event is in progress."*

#### For Stargazers 🌟
- Aurora alerts during geomagnetic storms
- Solar flare notifications for enhanced viewing
- Example: *"AURORA ALERT: G2 geomagnetic storm in progress! Enhanced aurora viewing opportunities."*

#### For Educators 📚
- Educational opportunities to discuss space weather
- All significant space weather events
- Example: *"EDUCATIONAL OPPORTUNITY: A great chance to discuss space weather with students."*

### 3. Real-time Monitoring

The backend periodically checks NOAA SWPC data feeds for:
- Radio blackouts (R-scale)
- Solar flares (M-class and X-class)
- Geomagnetic storms (G-scale)
- Solar radiation storms

## Setup Instructions

### 1. Database Setup

The migrations have already been created and applied. If you need to recreate them:

```bash
python3 manage.py makemigrations profiles
python3 manage.py migrate
```

### 2. Configure Settings

The context processor has been added to `settings.py`:

```python
TEMPLATES = [
    {
        'OPTIONS': {
            'context_processors': [
                # ... other processors
                'profiles.context_processors.active_alerts',
            ],
        },
    },
]
```

### 3. Set Up Periodic Alert Fetching

You can run the alert fetcher manually or set it up with a cron job.

#### Manual Execution

```bash
# Fetch real alerts
python3 manage.py fetch_space_weather

# Test mode (doesn't save to database)
python3 manage.py fetch_space_weather --test
```

#### Automated with Cron

Add to your crontab to check every 30 minutes:

```bash
*/30 * * * * cd /path/to/workspace && python3 manage.py fetch_space_weather >> /var/log/space_weather.log 2>&1
```

Or use Django's built-in management command scheduler, Celery, or a similar task queue.

### 4. Create Demo Alerts (Optional)

You can create test alerts via the Django admin panel or Django shell:

```python
from profiles.models import SolarAlert
from django.utils import timezone
from datetime import timedelta

# Create a sample alert for farmers
SolarAlert.objects.create(
    alert_type='solar_flare',
    severity='M',
    title='M2.5 Solar Flare Detected',
    description='A moderate M-class solar flare was detected. GPS systems may experience temporary disruptions.',
    is_active=True,
    expires_at=timezone.now() + timedelta(days=2),
    relevant_for_farmers=True,
    relevant_for_pilots=True,
    relevant_for_stargazers=True,
)

# Create a sample alert for pilots
SolarAlert.objects.create(
    alert_type='radio_blackout',
    severity='R3',
    title='R3 Radio Blackout Event',
    description='Strong radio blackout in progress. HF radio communications degraded.',
    is_active=True,
    expires_at=timezone.now() + timedelta(hours=12),
    relevant_for_pilots=True,
    relevant_for_farmers=True,
)

# Create a sample alert for stargazers
SolarAlert.objects.create(
    alert_type='geomagnetic_storm',
    severity='G2',
    title='Geomagnetic Storm Watch',
    description='Moderate geomagnetic storm in progress. Aurora viewing enhanced.',
    is_active=True,
    expires_at=timezone.now() + timedelta(days=1),
    relevant_for_stargazers=True,
    relevant_for_educators=True,
)
```

## User Guide

### For Users

1. **Set Your Preferences**
   - Navigate to your profile
   - Click "Edit Settings"
   - Select your interest/profession from the dropdown
   - Enable "Receive space weather alerts"
   - Click "Save Settings"

2. **View Alerts**
   - When relevant space weather events occur, you'll see a prominent banner at the top of the page
   - Alerts are color-coded by severity:
     - Red: Critical (pilots, severe events)
     - Yellow: Important (farmers, GPS issues)
     - Purple: Special (stargazers, aurora)
     - Blue: Informational (educators, general)
   - Click the X button to dismiss an alert

3. **Manage Alerts**
   - You can disable alerts anytime in your profile settings
   - Change your profession/interest to receive different types of alerts

### For Administrators

1. **Access the Admin Panel**
   - Navigate to `/admin/`
   - Go to "Profiles" section

2. **Manage User Profiles**
   - View all user preferences
   - Filter by profession or alert status
   - Manually update user settings if needed

3. **Manage Alerts**
   - View all active and past alerts
   - Create custom alerts for specific events
   - Mark alerts as active/inactive
   - Filter by type, severity, or target audience

4. **Monitor the System**
   - Check alert fetching logs
   - Review which alerts were delivered to which user groups
   - Deactivate old alerts manually if needed

## API Endpoints Used

The system fetches data from these NOAA SWPC JSON feeds:

- **Alerts Feed**: `https://services.swpc.noaa.gov/products/alerts.json`
- **Solar Flares**: `https://services.swpc.noaa.gov/json/goes/primary/xray-flares-latest.json`
- **NOAA Scales**: `https://services.swpc.noaa.gov/products/noaa-scales.json`

## Database Models

### UserProfile
- Links to Django User model (one-to-one)
- Stores profession/interest choice
- Alert opt-in preference
- Automatically created for all users

### SolarAlert
- Alert type (radio_blackout, solar_flare, geomagnetic_storm, solar_radiation)
- Severity level (R1-R5, G1-G5, M-class, X-class)
- Title and description
- Target audience flags
- Active/inactive status
- Expiration timestamp
- Raw data from SWPC (for reference)

## Technical Details

### Alert Matching Logic

The context processor (`profiles/context_processors.py`) filters alerts based on:
1. User authentication status
2. User's alert opt-in preference
3. User's selected profession
4. Alert's target audience flags
5. Alert active status and age (< 7 days)

### Alert Customization

Each alert type has profession-specific messaging via the `get_targeted_message()` method in the SolarAlert model. This ensures users receive relevant, actionable information.

### Performance Considerations

- Alerts are cached in the database to avoid excessive API calls
- Context processor runs on every page load but queries are optimized
- Duplicate detection prevents alert spam
- Old alerts are automatically deactivated after 7 days

## Troubleshooting

### Alerts Not Showing

1. Check user profile settings are saved
2. Verify alerts are enabled in profile
3. Confirm there are active alerts in the database
4. Check that alert targets match user's profession

### Space Weather Command Failing

1. Verify internet connectivity
2. Check NOAA SWPC API status
3. Review command output for specific errors
4. Try test mode first: `python3 manage.py fetch_space_weather --test`

### Template Issues

1. Ensure context processor is registered in settings.py
2. Clear browser cache
3. Check for JavaScript errors in browser console
4. Verify alert banner markup is correct

## Future Enhancements

Potential improvements for the system:

1. **Email/SMS Notifications**: Send alerts via email or text message
2. **Alert History**: Show users a history of past alerts they received
3. **Custom Alert Thresholds**: Let users choose severity levels
4. **Location-Based Alerts**: Filter by geographic location (for aurora viewing)
5. **Mobile App Integration**: Push notifications to mobile devices
6. **Alert Analytics**: Track which alerts get the most engagement
7. **Community Alerts**: Let users report space weather observations

## Support

For issues or questions:
- Check the admin panel for alert status
- Review management command logs
- Contact system administrator

## Credits

Space weather data provided by NOAA Space Weather Prediction Center (SWPC).

Alert system developed for the StellarSense platform.
