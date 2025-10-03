# Space Weather Alert System - Quick Setup Guide

## What Was Implemented

Your StellarSense platform now has a complete **Space Weather Alert System** with the following features:

### ✅ User Profile Enhancements
- Users can select their profession/interest: Stargazer, Farmer, Pilot, or Educator
- Simple dropdown in profile settings
- Opt-in/opt-out toggle for alerts

### ✅ Backend Monitor
- Django management command to fetch real-time SWPC data
- Monitors radio blackouts, solar flares, and geomagnetic storms
- Automatically categorizes alerts by severity and target audience

### ✅ Targeted Alert System
- **Farmers**: GPS disruption warnings
- **Pilots**: Radio blackout and aviation alerts
- **Stargazers**: Aurora and viewing opportunity notifications
- **Educators**: Educational opportunity alerts

### ✅ Visual Alert Banners
- Prominent, non-intrusive banners at the top of pages
- Color-coded by severity (red, yellow, purple, blue)
- Dismissible with smooth animations
- Only shown to opted-in users

## Quick Start

### 1. Access Profile Settings

1. Log in to your account
2. Click **PROFILE** in the navigation
3. Click **Edit Settings** button
4. Select your interest/profession from the dropdown
5. Ensure "Receive targeted space weather alerts" is checked
6. Click **Save Settings**

### 2. View Sample Alerts

Sample alerts have been created in the database. You should now see alert banners when you navigate to any page, customized for your selected profession.

### 3. Test Different Professions

Try changing your profession in settings to see different alert messages:
- **Farmer**: See GPS and agriculture-focused alerts
- **Pilot**: See aviation safety alerts
- **Stargazer**: See aurora and viewing opportunity alerts
- **Educator**: See educational opportunity alerts

## For Administrators

### Manage Alerts via Admin Panel

1. Navigate to `/admin/`
2. Go to **Profiles** → **Solar Alerts**
3. Here you can:
   - View all active and past alerts
   - Create custom alerts manually
   - Mark alerts as active/inactive
   - Filter by type, severity, or target audience

### Fetch Live Space Weather Data

Run the management command to fetch real-time data from NOAA:

```bash
# Test mode (preview without saving)
python3 manage.py fetch_space_weather --test

# Live mode (saves to database)
python3 manage.py fetch_space_weather
```

### Set Up Automated Monitoring

Add to crontab to check every 30 minutes:

```bash
crontab -e
```

Add this line:
```
*/30 * * * * cd /workspace && python3 manage.py fetch_space_weather >> /var/log/space_weather.log 2>&1
```

## Files Created/Modified

### New Files
- `/workspace/profiles/models.py` - UserProfile and SolarAlert models
- `/workspace/profiles/forms.py` - UserProfileForm
- `/workspace/profiles/context_processors.py` - Active alerts context processor
- `/workspace/profiles/management/commands/fetch_space_weather.py` - SWPC data fetcher
- `/workspace/profiles/templates/profiles/settings.html` - Profile settings page
- `/workspace/SPACE_WEATHER_ALERTS.md` - Complete documentation

### Modified Files
- `/workspace/profiles/views.py` - Added settings view
- `/workspace/profiles/urls.py` - Added settings route
- `/workspace/profiles/admin.py` - Registered new models
- `/workspace/profiles/templates/profiles/profile.html` - Added alert preferences display
- `/workspace/home/templates/base.html` - Added alert banner system
- `/workspace/StellarSense/settings.py` - Added context processor
- `/workspace/requirements.txt` - Added requests library

### Database
- New table: `profiles_userprofile`
- New table: `profiles_solaralert`

## Testing Checklist

- [x] User can access profile settings
- [x] User can select profession from dropdown
- [x] User can toggle alert preference
- [x] Settings are saved and persisted
- [x] Alert banners display for opted-in users
- [x] Alerts are filtered by user profession
- [x] Alert messages are customized per profession
- [x] Alerts can be dismissed
- [x] Management command fetches SWPC data
- [x] Admin panel shows all alerts
- [x] Sample alerts created successfully

## Example Alert Messages

### For Farmers 🚜
> **HEADS UP**: A recent M-class solar flare may cause GPS inaccuracies for the next 24-48 hours. Plan for potential disruptions in precision agriculture equipment.

### For Pilots ✈️
> **AVIATION ALERT**: An R3 (Strong) radio blackout event is in progress. Expect degradation of HF radio communication on the sunlit side of Earth.

### For Stargazers 🌟
> **AURORA ALERT**: G2 geomagnetic storm in progress! Enhanced aurora viewing opportunities at higher latitudes. Check local conditions for viewing.

### For Educators 📚
> **EDUCATIONAL OPPORTUNITY**: X1.2 Solar Flare Observed - A great chance to discuss space weather with students.

## Data Sources

All space weather data comes from **NOAA Space Weather Prediction Center (SWPC)**:
- Alerts Feed: https://services.swpc.noaa.gov/products/alerts.json
- Solar Flares: https://services.swpc.noaa.gov/json/goes/primary/xray-flares-latest.json
- NOAA Scales: https://services.swpc.noaa.gov/products/noaa-scales.json

## Support

For detailed documentation, see `/workspace/SPACE_WEATHER_ALERTS.md`

## Next Steps

1. **Set up automated monitoring**: Configure cron job to fetch data regularly
2. **Customize alert messages**: Edit the `get_targeted_message()` method in `profiles/models.py`
3. **Add more alert types**: Extend the model to include solar radiation storms
4. **Email notifications**: Integrate email sending for critical alerts
5. **Mobile integration**: Add push notifications for mobile users

---

🎉 **Your Space Weather Alert System is now live and ready to use!**
