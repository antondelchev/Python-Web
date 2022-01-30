from django.db import models


# Create your models here.

# for names: --> class JobTitle(models.Model) --> job_title in DB

class Employee(models.Model):
    first_name = models.CharField(
        max_length=30,
    )
    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
