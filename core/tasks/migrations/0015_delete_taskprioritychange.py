# Generated by Django 4.2.6 on 2023-11-16 09:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0014_delete_taskstatuschange"),
    ]

    operations = [
        migrations.DeleteModel(
            name="TaskPriorityChange",
        ),
    ]