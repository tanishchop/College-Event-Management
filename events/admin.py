from django.contrib import admin
from .models import Organizer, Event, Schedule, Slot

@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
    list_display = ['user', 'department']
    list_filter = ['department']
    search_fields = ['user__username', 'department']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'location', 'organizer']
    list_filter = ['organizer__department']
    search_fields = ['name', 'description']

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['title', 'event', 'start_time', 'end_time']
    list_filter = ['start_time']
    search_fields = ['title', 'description']

@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ['schedule', 'capacity']
    list_filter = ['schedule']
