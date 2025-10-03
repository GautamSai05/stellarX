from django.contrib import admin
from .models import UserProfile, SolarAlert


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'profession', 'receive_alerts', 'created_at', 'updated_at']
    list_filter = ['profession', 'receive_alerts', 'created_at']
    search_fields = ['user__username', 'user__email']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('User Information', {
            'fields': ('user',)
        }),
        ('Preferences', {
            'fields': ('profession', 'receive_alerts')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(SolarAlert)
class SolarAlertAdmin(admin.ModelAdmin):
    list_display = ['title', 'alert_type', 'severity', 'is_active', 'detected_at', 'get_target_audiences']
    list_filter = ['alert_type', 'severity', 'is_active', 'detected_at']
    search_fields = ['title', 'description']
    readonly_fields = ['detected_at', 'raw_data']
    date_hierarchy = 'detected_at'
    
    fieldsets = (
        ('Alert Information', {
            'fields': ('alert_type', 'severity', 'title', 'description')
        }),
        ('Status', {
            'fields': ('is_active', 'detected_at', 'event_time', 'expires_at')
        }),
        ('Target Audiences', {
            'fields': (
                'relevant_for_farmers',
                'relevant_for_pilots',
                'relevant_for_stargazers',
                'relevant_for_educators',
                'relevant_for_general'
            )
        }),
        ('Raw Data', {
            'fields': ('raw_data',),
            'classes': ('collapse',)
        }),
    )
    
    def get_target_audiences(self, obj):
        """Display which audiences this alert targets"""
        targets = []
        if obj.relevant_for_farmers:
            targets.append('Farmers')
        if obj.relevant_for_pilots:
            targets.append('Pilots')
        if obj.relevant_for_stargazers:
            targets.append('Stargazers')
        if obj.relevant_for_educators:
            targets.append('Educators')
        if obj.relevant_for_general:
            targets.append('General')
        return ', '.join(targets) if targets else 'None'
    get_target_audiences.short_description = 'Target Audiences'
    
    actions = ['mark_as_active', 'mark_as_inactive']
    
    def mark_as_active(self, request, queryset):
        """Mark selected alerts as active"""
        updated = queryset.update(is_active=True)
        self.message_user(request, f'{updated} alert(s) marked as active.')
    mark_as_active.short_description = 'Mark selected alerts as active'
    
    def mark_as_inactive(self, request, queryset):
        """Mark selected alerts as inactive"""
        updated = queryset.update(is_active=False)
        self.message_user(request, f'{updated} alert(s) marked as inactive.')
    mark_as_inactive.short_description = 'Mark selected alerts as inactive'
