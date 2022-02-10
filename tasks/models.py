from django.db import models
from users.models import User

class Task(models.Model):
    TYPE_OF_TASK = [
      ("finished", "finished"),
      ("pending", "pending"),
      ("overdue", "overdue"),
    ]
    user = models.ForeignKey(User, related_name="userTasks", on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    type_of_task = models.CharField(max_length=255, choices=TYPE_OF_TASK)
    description = models.TextField(null=True, blank=True)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"user: {self.user.username}"
