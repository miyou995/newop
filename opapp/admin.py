from django.contrib import admin
from .models import Meeting
# Register your models here.
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'subject', 'day', 'hour')
    list_display_links = ('id','name')
    list_editable = ['day', 'hour']
    list_per_page = 40
    search_fields = ('id', 'name', 'email', 'phone',)
admin.site.register(Meeting, MeetingAdmin)
