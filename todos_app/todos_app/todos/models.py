from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=28)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'people'


class Category(models.Model):
    CHOICE_HOME = 'Home'
    CHOICE_WORK = 'Work'
    NAME_CHOICES = (
        (CHOICE_HOME, '-- Home'),
        (CHOICE_WORK, '-- Work'),
    )

    name = models.CharField(
        max_length=30,
        choices=NAME_CHOICES,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Todo(models.Model):
    text = models.CharField(
        max_length=38,
    )
    state = models.BooleanField(
        default=False,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    owner = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        default=True,
    )
    category = models.ManyToManyField(Category)
