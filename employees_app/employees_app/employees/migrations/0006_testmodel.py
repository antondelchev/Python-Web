# Generated by Django 4.0.1 on 2022-01-30 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_employee_egn_alter_employee_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id2', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
            ],
        ),
    ]
