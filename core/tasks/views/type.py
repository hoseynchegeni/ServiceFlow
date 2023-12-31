from ..models import TaskType
from django.urls import reverse_lazy
from ..forms import CreateTaskTypeForm
from ..filters import TypeFilter
from .task import Task
from base.views import (
    BaseDeleteView,
    BaseListView,
    BaseCreateView,
    BaseUpdateView,
    BaseDetailView,
)


class TypeListView(BaseListView):
    model = TaskType
    context_object_name = "type"
    template_name = "tasks/type/list.html"
    filterset_class = TypeFilter
    permission_required = "tasks.view_tasktype"


class TypeDetailView(BaseDetailView):
    model = TaskType
    template_name = "tasks/type/detail.html"
    context_object_name = "type"
    permission_required = "tasks.view_tasktype"


class TypeCreateView(BaseCreateView):
    template_name = "tasks/type/create.html"
    form_class = CreateTaskTypeForm
    permission_required = "tasks.add_tasktype"
    success_message = "Task Type Successfully Created!"
    url = "tasks:detail_type"


class TypeUpdateView(BaseUpdateView):
    model = TaskType
    fields = ("name", "description", "is_active")
    template_name = "tasks/type/update.html"
    permission_required = "tasks.change_tasktype"
    success_message = "Task Type successfully updated!"
    url = "tasks:detail_type"


class TypeDeleteView(BaseDeleteView):
    model = TaskType
    template_name = "tasks/type/delete.html"
    success_url = reverse_lazy("tasks:list_type")
    message = "Task successfully Deleted!"
    permission_required = "task.delete_tasktype"


class TaskWithThisType(BaseDetailView):
    model = TaskType
    template_name = "tasks/type/task_type.html"
    context_object_name = "type"
    permission_required = "tasks.view_tasktype"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = Task.objects.filter(type_id=self.object.pk)
        return context
