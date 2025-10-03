# Space Weather Alerts - Quick Reference Card

## 🚀 Getting Started (3 Steps)

1. **Click** your profile in the navigation
2. **Click** "Edit Settings" button
3. **Select** your profession and save

That's it! You'll now see space weather alerts.

## 👤 Profession Types

| Profession | You'll See Alerts About |
|------------|------------------------|
| 🚜 **Farmer** | GPS disruptions affecting precision agriculture |
| ✈️ **Pilot** | Radio blackouts and radiation affecting aviation |
| 🌟 **Stargazer** | Aurora displays and solar activity |
| 📚 **Educator** | Educational opportunities about space weather |
| 🌍 **General** | All significant space weather events |

## 🎨 Alert Colors

| Color | Meaning | Example |
|-------|---------|---------|
| 🔴 **Red** | Critical/Urgent | Aviation safety alerts |
| 🟡 **Yellow** | Important/Warning | GPS disruptions |
| 🟣 **Purple** | Special/Opportunity | Aurora viewing |
| 🔵 **Blue** | Informational | Educational events |

## 📱 Alert Actions

- **X Button**: Dismiss this alert
- **Click Alert**: Read full details
- **Settings**: Turn alerts on/off

## ⚙️ Manage Preferences

**Location**: Profile → Edit Settings

**Options**:
- Change profession anytime
- Toggle alerts on/off
- View current settings

## 🔔 Alert Examples

### For Farmers
> "HEADS UP: M-class solar flare may cause GPS inaccuracies for 24-48 hours."

### For Pilots  
> "AVIATION ALERT: R3 radio blackout in progress. HF communication degraded."

### For Stargazers
> "AURORA ALERT: G2 storm in progress! Enhanced viewing at higher latitudes."

### For Educators
> "EDUCATIONAL OPPORTUNITY: X-class flare - great teaching moment!"

## 🛠️ Admin Commands

**Fetch Live Data**:
```bash
python3 manage.py fetch_space_weather
```

**Test Without Saving**:
```bash
python3 manage.py fetch_space_weather --test
```

**View Alerts**:
Navigate to: `/admin/profiles/solaralert/`

## 📊 Data Source

All data from **NOAA Space Weather Prediction Center**
- Official government source
- Real-time monitoring
- Updated every 30 minutes

## ❓ FAQ

**Q: How often are alerts updated?**  
A: New data is checked every 30 minutes (when automated)

**Q: Can I receive multiple alerts?**  
A: Yes, up to 3 most recent relevant alerts are shown

**Q: Do alerts disappear automatically?**  
A: Yes, they expire after the event passes or after 7 days

**Q: Can I change my profession later?**  
A: Absolutely! Update anytime in settings

**Q: What if I don't want alerts?**  
A: Just uncheck "Receive alerts" in your settings

## 🎯 Quick Tips

✅ Check your profession matches your actual needs  
✅ Alerts are only shown when you're logged in  
✅ Dismiss alerts you've read to clear the banner  
✅ Visit settings to see your current configuration  
✅ Admins can create custom alerts for special events  

## 📞 Need Help?

- **Documentation**: See `SPACE_WEATHER_ALERTS.md`
- **Setup Guide**: See `SETUP_GUIDE.md`
- **Admin**: Contact your system administrator

---

**Powered by NOAA SWPC** | **StellarSense Platform**
