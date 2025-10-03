from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    """Extended user profile with interests/profession for targeted alerts"""
    
    PROFESSION_CHOICES = [
        ('stargazer', 'Stargazer'),
        ('farmer', 'Farmer'),
        ('pilot', 'Pilot'),
        ('educator', 'Educator'),
        ('general', 'General Interest'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profession = models.CharField(
        max_length=20, 
        choices=PROFESSION_CHOICES, 
        default='general',
        help_text="Select your interest or profession for targeted space weather alerts"
    )
    receive_alerts = models.BooleanField(
        default=True,
        help_text="Receive space weather alerts relevant to your interests"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile ({self.get_profession_display()})"
    
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"


# Signal to automatically create UserProfile when a User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()


class SolarAlert(models.Model):
    """Store solar events and alerts from SWPC"""
    
    ALERT_TYPE_CHOICES = [
        ('radio_blackout', 'Radio Blackout'),
        ('solar_flare', 'Solar Flare'),
        ('geomagnetic_storm', 'Geomagnetic Storm'),
        ('solar_radiation', 'Solar Radiation Storm'),
    ]
    
    SEVERITY_CHOICES = [
        ('R1', 'R1 - Minor'),
        ('R2', 'R2 - Moderate'),
        ('R3', 'R3 - Strong'),
        ('R4', 'R4 - Severe'),
        ('R5', 'R5 - Extreme'),
        ('M', 'M-Class Flare'),
        ('X', 'X-Class Flare'),
        ('G1', 'G1 - Minor Storm'),
        ('G2', 'G2 - Moderate Storm'),
        ('G3', 'G3 - Strong Storm'),
        ('G4', 'G4 - Severe Storm'),
        ('G5', 'G5 - Extreme Storm'),
    ]
    
    alert_type = models.CharField(max_length=20, choices=ALERT_TYPE_CHOICES)
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    detected_at = models.DateTimeField(auto_now_add=True)
    event_time = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    
    # Target audiences
    relevant_for_farmers = models.BooleanField(default=False)
    relevant_for_pilots = models.BooleanField(default=False)
    relevant_for_stargazers = models.BooleanField(default=False)
    relevant_for_educators = models.BooleanField(default=False)
    relevant_for_general = models.BooleanField(default=True)
    
    # Raw data for reference
    raw_data = models.JSONField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.get_alert_type_display()} - {self.severity} ({self.detected_at.strftime('%Y-%m-%d %H:%M')})"
    
    class Meta:
        verbose_name = "Solar Alert"
        verbose_name_plural = "Solar Alerts"
        ordering = ['-detected_at']
        indexes = [
            models.Index(fields=['-detected_at']),
            models.Index(fields=['is_active']),
        ]
    
    def get_targeted_message(self, profession):
        """Return a customized message based on user profession"""
        messages = {
            'farmer': self._get_farmer_message(),
            'pilot': self._get_pilot_message(),
            'stargazer': self._get_stargazer_message(),
            'educator': self._get_educator_message(),
            'general': self.description,
        }
        return messages.get(profession, self.description)
    
    def _get_farmer_message(self):
        if self.alert_type == 'solar_flare' and 'M' in self.severity:
            return f"HEADS UP: A recent {self.severity}-class solar flare may cause GPS inaccuracies for the next 24-48 hours. Plan for potential disruptions in precision agriculture equipment."
        elif self.alert_type == 'radio_blackout':
            return f"FARMER ALERT: {self.severity} radio blackout event detected. GPS and communication systems may experience interference. Consider backup navigation methods."
        return self.description
    
    def _get_pilot_message(self):
        if self.alert_type == 'radio_blackout' and any(level in self.severity for level in ['R3', 'R4', 'R5']):
            return f"AVIATION ALERT: An {self.severity} ({self.get_severity_display()}) radio blackout event is in progress. Expect degradation of HF radio communication on the sunlit side of Earth."
        elif self.alert_type == 'solar_radiation':
            return f"AVIATION ALERT: {self.severity} solar radiation storm detected. Polar routes may be affected. Monitor radiation levels and consider altitude/route adjustments."
        return self.description
    
    def _get_stargazer_message(self):
        if self.alert_type == 'geomagnetic_storm':
            return f"AURORA ALERT: {self.severity} geomagnetic storm in progress! Enhanced aurora viewing opportunities at higher latitudes. Check local conditions for viewing."
        elif self.alert_type == 'solar_flare':
            return f"SOLAR ACTIVITY: {self.severity}-class solar flare detected. May enhance aurora displays in the coming days. Keep watching the skies!"
        return self.description
    
    def _get_educator_message(self):
        return f"EDUCATIONAL OPPORTUNITY: {self.title} - A great chance to discuss space weather with students. {self.description}"
