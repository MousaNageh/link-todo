from rest_framework import serializers
from .models import Task

class TasksListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
          "start_date",
          "due_date",
          "type_of_task",
          "description",
          "is_complete",
          "created_at",
          "updated_at",
        ]