# Generated by Django 4.0.1 on 2022-02-01 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0017_alter_employee_options_department_created_on_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='updated_on',
        ),
    ]