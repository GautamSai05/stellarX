from django.contrib import admin
from .models import AlertEvent


@admin.register(AlertEvent)
class AlertEventAdmin(admin.ModelAdmin):
    list_display = ("title", "audience", "severity", "active", "starts_at", "ends_at")
    list_filter = ("audience", "severity", "active")
    search_fields = ("title", "message", "source_id")
