from django.db import models
from uuid import uuid4

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField()
    assignee = models.CharField(max_length=200)
    status = models.CharField(max_length=50)