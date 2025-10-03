import json
from datetime import datetime, timedelta
from typing import Optional

import requests
from django.core.management.base import BaseCommand
from django.utils import timezone

from alerts.models import AlertEvent, AlertAudience


SWPC_ALERTS_URL = "https://services.swpc.noaa.gov/products/alerts.json"


def parse_swpc_item(item: dict) -> Optional[dict]:
    # products/alerts.json schema: list of dicts with keys: product_id, issue_datetime, message
    message: str = item.get("message", "") or ""
    product_id: str = str(item.get("product_id") or "")
    issued_at_str: str = item.get("issue_datetime") or ""

    if not product_id or not message:
        return None

    severity = ""
    audience = AlertAudience.ANY
    title = "Space Weather Notification"
    custom_message: Optional[str] = None

    lower_msg = message.lower()
    if "r3" in lower_msg or "strong radio blackout" in lower_msg:
        severity = "R3"
        audience = AlertAudience.PILOT
        title = "Pilot's Alert"
        custom_message = (
            "AVIATION ALERT: An R3 (Strong) radio blackout event is in progress. "
            "Expect degradation of HF radio communication on the sunlit side of Earth."
        )
    elif "r2" in lower_msg or "moderate radio blackout" in lower_msg:
        severity = "R2"
        audience = AlertAudience.PILOT
        title = "Aviation Alert: R2 radio blackout"
    elif "m-class" in lower_msg or (" m" in lower_msg and "flare" in lower_msg):
        severity = "M-class"
        audience = AlertAudience.FARMER
        title = "Farmer's Alert"
        custom_message = (
            "HEADS UP: A recent M-class solar flare may cause GPS inaccuracies for the next 24-48 hours. "
            "Plan for potential disruptions in precision agriculture equipment."
        )
    elif "x-class" in lower_msg or " x" in lower_msg and "flare" in lower_msg:
        severity = "X-class"
        audience = AlertAudience.PILOT
        title = "Critical: X-class solar flare"

    if severity == "":
        return None

    starts_at: Optional[datetime] = None
    if issued_at_str:
        try:
            # Example format: '2025-10-03 12:15:13.110'
            starts_at = datetime.strptime(issued_at_str.split(".")[0], "%Y-%m-%d %H:%M:%S")
            starts_at = starts_at.replace(tzinfo=timezone.utc)
        except Exception:
            starts_at = None

    ends_at = None
    if severity in {"M-class", "X-class"}:
        ends_at = (starts_at or timezone.now()) + timedelta(hours=48)
    elif severity in {"R2", "R3"}:
        ends_at = (starts_at or timezone.now()) + timedelta(hours=12)

    return {
        "source_id": f"{product_id}:{issued_at_str}",
        "title": title,
        "message": custom_message or message,
        "audience": audience,
        "severity": severity,
        "starts_at": starts_at,
        "ends_at": ends_at,
    }


class Command(BaseCommand):
    help = "Fetch SWPC notifications and store targeted AlertEvent records"

    def handle(self, *args, **options):
        try:
            resp = requests.get(SWPC_ALERTS_URL, timeout=15)
            resp.raise_for_status()
            data = resp.json()
        except Exception as exc:
            self.stderr.write(self.style.ERROR(f"Failed to fetch SWPC feed: {exc}"))
            return

        created_count = 0
        updated_count = 0
        for item in data:
            parsed = parse_swpc_item(item)
            if not parsed:
                continue

            obj, created = AlertEvent.objects.update_or_create(
                source_id=parsed["source_id"],
                defaults={
                    "title": parsed["title"],
                    "message": parsed["message"],
                    "audience": parsed["audience"],
                    "severity": parsed["severity"],
                    "starts_at": parsed["starts_at"],
                    "ends_at": parsed["ends_at"],
                    "active": True,
                },
            )
            if created:
                created_count += 1
            else:
                updated_count += 1

        self.stdout.write(self.style.SUCCESS(f"SWPC monitor completed: created={created_count}, updated={updated_count}"))
