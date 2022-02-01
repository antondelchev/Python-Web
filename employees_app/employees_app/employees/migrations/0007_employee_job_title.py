# Generated by Django 4.0.1 on 2022-01-30 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_testmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='job_title',
            field=models.CharField(choices=[('Web Developer', 1), ('QA', 2), ('DevOps', 3)], default='', max_length=30),
            preserve_default=False,
        ),
    ]