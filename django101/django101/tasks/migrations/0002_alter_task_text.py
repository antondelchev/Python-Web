# Generated by Django 4.0.1 on 2022-01-20 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='text',
            field=models.CharField(max_length=150),
        ),
    ]
