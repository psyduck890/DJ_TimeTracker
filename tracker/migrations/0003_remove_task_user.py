# Generated by Django 5.0.4 on 2024-05-04 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_task_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]