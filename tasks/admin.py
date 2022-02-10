from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "start_date",
        "due_date",
        "type_of_task",
        "description",
        "is_complete",
        "created_at",
        "updated_at",
    )

    search_fields = ['user__username']
    list_filter = [
         "user__username",
         "type_of_task",
    ]
    date_hierarchy = 'created_at'