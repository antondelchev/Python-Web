from django.db import models


# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(

    )

    last_name = models.CharField(

    )

    budget = models.FloatField(

    )

    image = models.ImageField(
        
    )


class Expense(models.Model):
    pass
