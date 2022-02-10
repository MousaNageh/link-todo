from django.db import models
from users.models import User

class Task(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    TYPE_OF_TASK = [
      ("finished", "finished"),
      ("pending", "pending"),
      ("overdue", "overdue"),
    ]
    user = models.ForeignKey(User, related_name="userTasks", on_delete=models.CASCADE)
    startDate = models.DateTimeField()
    dueDate = models.DateTimeField()
    typeOfTask = models.CharField(max_length=255, choices=TYPE_OF_TASK)
    isComplete = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"user: {self.user.username}"
