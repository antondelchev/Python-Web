# Generated by Django 4.0.1 on 2022-01-30 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='last_name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
