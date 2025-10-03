from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "profession", "alert_opt_in")
    search_fields = ("user__username", "user__email")
    list_filter = ("profession", "alert_opt_in")
