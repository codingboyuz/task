import uuid

from shared.models import BaseModel
from django.db import models

from tasklist.models import Task


class SubTask(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task = models.ForeignKey(Task, related_name="sub_tasks", on_delete=models.CASCADE)  # Task bilan bog‘lanish
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('in_progress', 'In Progress'),
                                                      ('completed', 'Completed')])
    priority = models.CharField(max_length=10, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
    due_date = models.DateTimeField(null=True, blank=True)