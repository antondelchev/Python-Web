from django.db import models


# Create your models here.

class Department(models.Model):
    name = models.CharField(
        max_length=30,
    )


class Employee(models.Model):
    WEB_DEVELOPER = 1
    QA = 2
    DEV_OPS = 3

    GOOGLE = 'Google'
    SOFT_UNI = 'Softuni'

    COMPANIES = (
        GOOGLE,
        SOFT_UNI
    )

    first_name = models.CharField(
        max_length=30,
    )
    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    egn = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='EGN',
    )
    job_title = models.IntegerField(
        choices=(
            (WEB_DEVELOPER, 'Web Developer'),
            (QA, 'QA'),
            (DEV_OPS, 'DevOps'),
        ),
    )

    company = models.CharField(
        max_length=max(len(i) for i in COMPANIES),
        choices=((c, c) for c in COMPANIES)  # geez
    )

    # one to many
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )


class Project(models.Model):
    name = models.CharField(
        max_length=30,
    )
    dead_line = models.DateField(
        null=True,
        blank=True,
    )

    # employeeS --> PLURAL
    # many to many
    employees = models.ManyToManyField(
        to=Employee,
    )  # ----> many to many -> exists only in one of the tables that are related, doesn't matter which one


class User(models.Model):
    email = models.EmailField()

    # one to one
    employee = models.OneToOneField(
        to=Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )

# class TestModel(models.Model):
#     id2 = models.IntegerField(
#         auto_created=True,
#         primary_key=True,
#     )
