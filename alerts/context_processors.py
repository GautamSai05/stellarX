from typing import Dict, Any
from django.utils import timezone
from django.db.models import Q
from .models import AlertEvent


def active_alert_banner(request) -> Dict[str, Any]:
    if not request.user.is_authenticated:
        return {}

    user_profile = getattr(request.user, "profile", None)
    if user_profile is None or not user_profile.alert_opt_in:
        return {}

    audience_key = user_profile.profession or "any"

    now = timezone.now()
    alerts = (
        AlertEvent.objects.filter(active=True)
        .filter(Q(audience="any") | Q(audience=audience_key))
        .filter(Q(starts_at__isnull=True) | Q(starts_at__lte=now))
        .filter(Q(ends_at__isnull=True) | Q(ends_at__gte=now))
        .order_by("-created_at")
    )

    if alerts.exists():
        return {"active_alert": alerts.first()}

    return {}
