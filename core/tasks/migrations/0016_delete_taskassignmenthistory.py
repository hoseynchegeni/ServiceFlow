# Generated by Django 4.2.6 on 2023-11-16 09:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0015_delete_taskprioritychange"),
    ]

    operations = [
        migrations.DeleteModel(
            name="TaskAssignmentHistory",
        ),
    ]
