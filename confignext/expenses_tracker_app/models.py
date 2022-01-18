from django.db import models


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    budget = models.IntegerField(default=None)

    class Meta:
        verbose_name_plural = 'Profiles'


class Expenses(models.Model):
    title = models.CharField(max_length=50)
    image_url = models.URLField(default=None)
    description = models.TextField(default=None)
    price = models.FloatField(default=None)

    class Meta:
        verbose_name_plural = 'Expenses'
