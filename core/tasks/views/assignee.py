from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect
from django.views import View
from django.contrib import messages
from ..models import Task
from db_events.models import TaskLog
from django.contrib.auth.mixins import LoginRequiredMixin
from base.views import BaseUpdateView


class TaskAssignToMe(LoginRequiredMixin, View):
    def get(self, request, pk):
        task = Task.objects.filter(pk=pk).first()
        if task:
            if task.team in self.request.user.groups.all():
                task.assign_to = self.request.user
                task.participants.add(self.request.user)
                messages.success(
                    self.request, f"TSK-{task.id} Successfully assigned to you."
                )
                task.save()
                TaskLog.objects.create(
                    user=self.request.user,
                    task=task,
                    event_type="Assignment",
                    additional_info=f"{self.request.user} Assigned Task to {task.assign_to}",
                )
            else:
                messages.warning(
                    self.request, f"You Cant Assign TSK-{task.id} to your self, its not assigned to your team."
                )
        return HttpResponseRedirect(
            reverse_lazy("tasks:detail", kwargs={"pk": task.pk})
        )
        


class TaskAssignTo(BaseUpdateView):
    template_name = "tasks/assign_to.html"
    model = Task
    fields = ("assign_to",)
    success_message = "Task successfully assigned."
    permission_required = "tasks.change_task"
    url = "tasks:detail"

    def form_valid(self, form):
        task = form.save(commit=False)
        task.save()
        task.participants.add(task.assign_to)
        task.participants.add(self.request.user)
        task.save()

        TaskLog.objects.create(
            user=self.request.user,
            task=task,
            event_type="Assignment",
            additional_info=f"{self.request.user} Assigned Task to {task.assign_to}",
        )
        return super().form_valid(form)
