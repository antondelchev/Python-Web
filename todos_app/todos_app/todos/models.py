from django.db import models


class Todo(models.Model):
    text = models.CharField(max_length=28)
    state = models.BooleanField(default=False)
    completed_by = models.CharField(max_length=38, null=True)
