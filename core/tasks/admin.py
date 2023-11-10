from django.contrib import admin
from .models import Task, TaskStatus, TaskType, TaskAssignmentHistory

# Register your models here.
admin.site.register(Task)
admin.site.register(TaskType)
admin.site.register(TaskStatus)
admin.site.register(TaskAssignmentHistory)
