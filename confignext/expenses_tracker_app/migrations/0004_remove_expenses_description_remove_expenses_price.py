# Generated by Django 4.0.1 on 2022-01-18 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses_tracker_app', '0003_expenses_description_expenses_image_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expenses',
            name='description',
        ),
        migrations.RemoveField(
            model_name='expenses',
            name='price',
        ),
    ]
