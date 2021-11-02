from django.contrib import admin
from django.utils import timezone
from .models import LoginHistoryTracker
# Register your models here.

@admin.register(LoginHistoryTracker)
class LoginHistoryTrackerAdmin(admin.ModelAdmin):
    """
    Registering in admin panel
    """

    list_display = ['action','username','ip','user_agent','date_time']
    list_filter = ['action','username','date_time']
    readonly_fields = [field.name for field in LoginHistoryTracker._meta.get_fields()]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def days_since_created(self):
        diff = timezone.now - self.date_time
        return diff.days