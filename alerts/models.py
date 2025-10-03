from django.db import models
from django.utils import timezone


class AlertAudience(models.TextChoices):
    ANY = "any", "Any"
    STARGAZER = "stargazer", "Stargazer"
    FARMER = "farmer", "Farmer"
    PILOT = "pilot", "Pilot"
    EDUCATOR = "educator", "Educator"


class AlertEvent(models.Model):
    source_id = models.CharField(max_length=128, unique=True)
    title = models.CharField(max_length=255)
    message = models.TextField()
    audience = models.CharField(max_length=20, choices=AlertAudience.choices, default=AlertAudience.ANY)
    severity = models.CharField(max_length=32, blank=True, default="")
    starts_at = models.DateTimeField(null=True, blank=True)
    ends_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def is_active(self) -> bool:
        now = timezone.now()
        if not self.active:
            return False
        if self.starts_at and self.starts_at > now:
            return False
        if self.ends_at and self.ends_at < now:
            return False
        return True

    def __str__(self) -> str:
        return f"{self.title} [{self.severity}] -> {self.audience}"
