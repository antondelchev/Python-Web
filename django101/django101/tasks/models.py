from django.db import models


# Create your models here.

class Task(models.Model):
    title = models.CharField(
        max_length=15,
        null=False
    )
    text = models.CharField(
        max_length=150,
    )


class Category(models.Model):
    name = models.CharField(
        max_length=20,
    )
