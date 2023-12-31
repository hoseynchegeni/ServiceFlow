import django_filters
from django_filters import FilterSet
from .models import Task, TaskPriority, TaskStatus, TaskType


class TaskFilter(FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    assign_to = django_filters.CharFilter(field_name="assign_to__email",)
    created_by = django_filters.CharFilter(field_name="created_by__email",)

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "created_by",
            "type",
            "status",
            "assign_to",
        ]


class PriorityFilter(FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = TaskPriority
        fields = [
            "id",
            "name",
        ]


class StatusFilter(FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = TaskStatus
        fields = [
            "id",
            "name",
        ]


class TypeFilter(FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = TaskType
        fields = [
            "id",
            "name",
        ]
