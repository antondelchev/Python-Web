# Generated by Django 4.0.1 on 2022-01-18 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses_tracker_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expenses',
            options={'verbose_name_plural': 'Expenses'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name_plural': 'Profiles'},
        ),
    ]
