from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """Extended profile settings per user."""

    class Profession(models.TextChoices):
        STARGAZER = "stargazer", "Stargazer"
        FARMER = "farmer", "Farmer"
        PILOT = "pilot", "Pilot"
        EDUCATOR = "educator", "Educator"

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profession = models.CharField(
        max_length=20,
        choices=Profession.choices,
        blank=True,
        default="",
        help_text="Select your primary interest/profession to tailor alerts.",
    )
    alert_opt_in = models.BooleanField(
        default=True,
        help_text="Receive targeted space weather alerts relevant to you.",
    )

    def __str__(self) -> str:
        return f"Profile({self.user.username})"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance: User, created: bool, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance: User, **kwargs):
    # Ensure profile exists and is saved when user saves
    UserProfile.objects.get_or_create(user=instance)
