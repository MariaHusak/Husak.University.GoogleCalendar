from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'start_time', 'end_time', 'event_type', 'category', 'creator')
    list_filter = ('date', 'event_type', 'category', 'creator')
    search_fields = ('title', 'description', 'location', 'creator__username')
    ordering = ('date',)

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'location', 'event_type', 'category')
        }),
        ('Time Information', {
            'fields': ('date', 'start_time', 'end_time', 'recurrence')
        }),
        ('Participants', {
            'fields': ('creator', 'invited_users', 'attendees')
        }),
    )

    readonly_fields = ('id',)


admin.site.register(Event, EventAdmin)
