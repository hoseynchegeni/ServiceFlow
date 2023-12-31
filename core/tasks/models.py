from django.db import models
from accounts.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import Group
# Create your models here.


def generate_pk():
    pass


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reaporter"
    )
    type = models.ForeignKey(
        "TaskType", on_delete=models.SET_NULL, blank=True, null=True
    )
    created_date = models.DateTimeField(auto_now_add=True)
    last_change = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(
        "TaskStatus", on_delete=models.SET_NULL, blank=True, null=True
    )
    current_state = models.ForeignKey("flow.State", on_delete=models.SET_NULL, blank = True, null = True)
    process_percentage = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])

    assign_to = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, related_name="Assigner"
    )
    team  = models.ForeignKey(Group, on_delete=models.SET_NULL, blank = True, null = True,)
    priority = models.ForeignKey(
        "TaskPriority", on_delete=models.SET_NULL, blank=True, null=True
    )
    participants = models.ManyToManyField(
        User, related_name="tasks_participated", blank=True
    )
    actions = models.ManyToManyField('flow.Action',blank= True)

    def __str__(self):
        return self.title


class TaskType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    work_flow = models.OneToOneField('flow.WorkFlow', on_delete = models.SET_NULL, blank = True, null = True)
    created_by = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class TaskStatus(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class TaskPriority(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    badge = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class TaskComment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    commented_at = models.DateTimeField(auto_now_add=True)
    attachment_title = models.CharField(
        max_length=50, default="attachment", blank=True, null=True
    )
    attachments = models.FileField(upload_to="attachments", blank=True, null=True)

    def __str__(self):
        return f"{self.task.title}/ {self.user.email}"



class TaskLogFlow(models.Model):
    task = models.ForeignKey('Task', on_delete = models.CASCADE, related_name = 'flow_task')
    flow = models.ForeignKey('flow.WorkFlow', on_delete = models.CASCADE, related_name = 'flow_flow', blank=True, null=True)
    state = models.ForeignKey('flow.State', on_delete = models.CASCADE, related_name = 'flow_state', blank=True, null=True)
    comment = models.CharField(max_length = 255, blank = True, null = True)
    attachments_1 = models.FileField(upload_to="attachments", blank=True, null=True)
    attachments_2 = models.FileField(upload_to="attachments", blank=True, null=True)
    attachments_3 = models.FileField(upload_to="attachments", blank=True, null=True)
    action = models.ForeignKey('flow.Action', blank = True, null = True, on_delete = models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Task: {self.task}, Flow: {self.flow}, State: {self.state}"