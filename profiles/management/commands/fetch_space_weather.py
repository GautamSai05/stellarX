"""
Management command to fetch and process space weather data from NOAA SWPC.
Run this command periodically (e.g., via cron) to monitor for solar events.
"""

from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
import requests
import json
from profiles.models import SolarAlert


class Command(BaseCommand):
    help = 'Fetch space weather alerts from NOAA SWPC and create targeted alerts'

    def add_arguments(self, parser):
        parser.add_argument(
            '--test',
            action='store_true',
            help='Run in test mode and display data without saving',
        )

    def handle(self, *args, **options):
        test_mode = options['test']
        
        self.stdout.write(self.style.SUCCESS('Fetching space weather data from NOAA SWPC...'))
        
        # NOAA SWPC provides several JSON feeds
        feeds = {
            'alerts': 'https://services.swpc.noaa.gov/products/alerts.json',
            'solar_flares': 'https://services.swpc.noaa.gov/json/goes/primary/xray-flares-latest.json',
            'geomagnetic': 'https://services.swpc.noaa.gov/products/noaa-scales.json',
        }
        
        alerts_created = 0
        
        # Fetch current alerts
        try:
            alerts_created += self._process_alerts_feed(feeds['alerts'], test_mode)
            alerts_created += self._process_solar_flares(feeds['solar_flares'], test_mode)
            alerts_created += self._process_geomagnetic_data(feeds['geomagnetic'], test_mode)
            
            if test_mode:
                self.stdout.write(self.style.WARNING(f'TEST MODE: Would have created {alerts_created} new alerts'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Successfully created {alerts_created} new alerts'))
                
                # Deactivate old alerts (older than 7 days)
                cutoff_date = timezone.now() - timedelta(days=7)
                old_alerts = SolarAlert.objects.filter(is_active=True, detected_at__lt=cutoff_date)
                count = old_alerts.count()
                old_alerts.update(is_active=False)
                self.stdout.write(self.style.SUCCESS(f'Deactivated {count} old alerts'))
                
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error fetching space weather data: {str(e)}'))

    def _process_alerts_feed(self, url, test_mode):
        """Process the SWPC alerts feed"""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            alerts = response.json()
            
            created_count = 0
            
            for alert in alerts:
                # Extract relevant information
                message = alert.get('message', '')
                issue_time = alert.get('issue_datetime')
                
                # Determine alert type and severity from message
                alert_type, severity, targets = self._parse_alert_message(message)
                
                if alert_type and not test_mode:
                    # Check if this alert already exists (avoid duplicates)
                    existing = SolarAlert.objects.filter(
                        title=message[:200],
                        detected_at__gte=timezone.now() - timedelta(hours=1)
                    ).exists()
                    
                    if not existing:
                        SolarAlert.objects.create(
                            alert_type=alert_type,
                            severity=severity,
                            title=message[:200],
                            description=message,
                            is_active=True,
                            expires_at=timezone.now() + timedelta(days=2),
                            raw_data=alert,
                            **targets
                        )
                        created_count += 1
                        self.stdout.write(self.style.SUCCESS(f'  Created alert: {message[:80]}...'))
                elif test_mode and alert_type:
                    self.stdout.write(self.style.WARNING(f'  TEST: Would create alert: {message[:80]}...'))
                    created_count += 1
            
            return created_count
            
        except requests.RequestException as e:
            self.stdout.write(self.style.ERROR(f'  Error fetching alerts feed: {str(e)}'))
            return 0

    def _process_solar_flares(self, url, test_mode):
        """Process solar flare data"""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            flares = response.json()
            
            created_count = 0
            recent_cutoff = timezone.now() - timedelta(hours=24)
            
            for flare in flares[:5]:  # Process only the 5 most recent
                flare_class = flare.get('current_class', '')
                begin_time = flare.get('begin_time')
                max_time = flare.get('max_time')
                
                # Only process M-class and X-class flares
                if flare_class and (flare_class.startswith('M') or flare_class.startswith('X')):
                    severity = 'M' if flare_class.startswith('M') else 'X'
                    
                    title = f"{flare_class} Solar Flare Detected"
                    description = f"A {flare_class}-class solar flare was detected at {max_time or begin_time}. This event may cause temporary radio blackouts and GPS disruptions."
                    
                    if not test_mode:
                        existing = SolarAlert.objects.filter(
                            alert_type='solar_flare',
                            severity=severity,
                            detected_at__gte=recent_cutoff
                        ).exists()
                        
                        if not existing:
                            SolarAlert.objects.create(
                                alert_type='solar_flare',
                                severity=severity,
                                title=title,
                                description=description,
                                is_active=True,
                                expires_at=timezone.now() + timedelta(days=2),
                                raw_data=flare,
                                relevant_for_farmers=True,
                                relevant_for_pilots=True,
                                relevant_for_stargazers=True,
                                relevant_for_educators=True,
                                relevant_for_general=True,
                            )
                            created_count += 1
                            self.stdout.write(self.style.SUCCESS(f'  Created flare alert: {title}'))
                    else:
                        self.stdout.write(self.style.WARNING(f'  TEST: Would create flare alert: {title}'))
                        created_count += 1
            
            return created_count
            
        except requests.RequestException as e:
            self.stdout.write(self.style.ERROR(f'  Error fetching solar flare data: {str(e)}'))
            return 0

    def _process_geomagnetic_data(self, url, test_mode):
        """Process geomagnetic storm data"""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            created_count = 0
            
            # Check for geomagnetic storms
            if 'G' in data:
                g_scale = data['G']
                current_level = g_scale.get('Scale', 'G0')
                
                if current_level != 'G0':
                    title = f"Geomagnetic Storm Watch: {current_level}"
                    description = f"A {current_level} geomagnetic storm is in progress. Aurora viewing may be enhanced at higher latitudes."
                    
                    if not test_mode:
                        existing = SolarAlert.objects.filter(
                            alert_type='geomagnetic_storm',
                            severity=current_level,
                            detected_at__gte=timezone.now() - timedelta(hours=6)
                        ).exists()
                        
                        if not existing:
                            SolarAlert.objects.create(
                                alert_type='geomagnetic_storm',
                                severity=current_level,
                                title=title,
                                description=description,
                                is_active=True,
                                expires_at=timezone.now() + timedelta(days=1),
                                raw_data=data,
                                relevant_for_stargazers=True,
                                relevant_for_educators=True,
                                relevant_for_general=True,
                            )
                            created_count += 1
                            self.stdout.write(self.style.SUCCESS(f'  Created geomagnetic alert: {title}'))
                    else:
                        self.stdout.write(self.style.WARNING(f'  TEST: Would create geomagnetic alert: {title}'))
                        created_count += 1
            
            # Check for radio blackouts
            if 'R' in data:
                r_scale = data['R']
                current_level = r_scale.get('Scale', 'R0')
                
                if current_level in ['R2', 'R3', 'R4', 'R5']:
                    title = f"Radio Blackout Alert: {current_level}"
                    description = f"A {current_level} radio blackout event is in progress. HF radio communications may be degraded."
                    
                    if not test_mode:
                        existing = SolarAlert.objects.filter(
                            alert_type='radio_blackout',
                            severity=current_level,
                            detected_at__gte=timezone.now() - timedelta(hours=3)
                        ).exists()
                        
                        if not existing:
                            SolarAlert.objects.create(
                                alert_type='radio_blackout',
                                severity=current_level,
                                title=title,
                                description=description,
                                is_active=True,
                                expires_at=timezone.now() + timedelta(hours=12),
                                raw_data=data,
                                relevant_for_farmers=True,
                                relevant_for_pilots=True,
                                relevant_for_educators=True,
                                relevant_for_general=True,
                            )
                            created_count += 1
                            self.stdout.write(self.style.SUCCESS(f'  Created radio blackout alert: {title}'))
                    else:
                        self.stdout.write(self.style.WARNING(f'  TEST: Would create radio blackout alert: {title}'))
                        created_count += 1
            
            return created_count
            
        except requests.RequestException as e:
            self.stdout.write(self.style.ERROR(f'  Error fetching geomagnetic data: {str(e)}'))
            return 0
        except (KeyError, TypeError) as e:
            self.stdout.write(self.style.ERROR(f'  Error parsing geomagnetic data: {str(e)}'))
            return 0

    def _parse_alert_message(self, message):
        """Parse alert message to determine type, severity, and target audiences"""
        message_lower = message.lower()
        
        alert_type = None
        severity = 'R1'
        targets = {
            'relevant_for_farmers': False,
            'relevant_for_pilots': False,
            'relevant_for_stargazers': False,
            'relevant_for_educators': False,
            'relevant_for_general': True,
        }
        
        # Determine alert type
        if 'radio blackout' in message_lower or 'r2' in message_lower or 'r3' in message_lower:
            alert_type = 'radio_blackout'
            targets['relevant_for_farmers'] = True
            targets['relevant_for_pilots'] = True
            targets['relevant_for_educators'] = True
            
            # Extract severity
            for level in ['R5', 'R4', 'R3', 'R2', 'R1']:
                if level.lower() in message_lower:
                    severity = level
                    break
                    
        elif 'geomagnetic storm' in message_lower or 'aurora' in message_lower:
            alert_type = 'geomagnetic_storm'
            targets['relevant_for_stargazers'] = True
            targets['relevant_for_educators'] = True
            
            for level in ['G5', 'G4', 'G3', 'G2', 'G1']:
                if level.lower() in message_lower:
                    severity = level
                    break
                    
        elif 'solar flare' in message_lower or 'x-ray' in message_lower:
            alert_type = 'solar_flare'
            targets['relevant_for_farmers'] = True
            targets['relevant_for_pilots'] = True
            targets['relevant_for_stargazers'] = True
            targets['relevant_for_educators'] = True
            
            if 'x-class' in message_lower or 'x class' in message_lower:
                severity = 'X'
            elif 'm-class' in message_lower or 'm class' in message_lower:
                severity = 'M'
                
        elif 'radiation' in message_lower and 'storm' in message_lower:
            alert_type = 'solar_radiation'
            targets['relevant_for_pilots'] = True
            targets['relevant_for_educators'] = True
        
        return alert_type, severity, targets
