from django.contrib import admin
from .models import Meetings, MeetingStatus

# Register your models here.

admin.site.register(Meetings)
admin.site.register(MeetingStatus)
