from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=28)


class Categories(models.Model):
    name = models.CharField(max_length=20)


class Todo(models.Model):
    text = models.CharField(max_length=28)
    state = models.BooleanField(default=False)
    owner = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        default=True,
    )
    category = models.ManyToManyField(Categories)
