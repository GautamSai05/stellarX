import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "StellarSense.settings")
django.setup()

from calender.models import AstronomicalEvent

events = [
    {"date": "2024-04-01", "description": "There were no widely notable astronomical events on April 1st, 2024."},
    {"date": "2024-04-07", "description": "There were no widely notable astronomical events on April 7, 2024. There are no significant meteor showers, eclipses, or planetary alignments on that date."},
    {"date": "2024-04-12", "description": "There were no widely notable astronomical events on April 12, 2024. The date falls between major meteor showers and eclipses."}
]

for event in events:
    AstronomicalEvent.objects.get_or_create(date=event['date'], defaults={'description': event['description']})
