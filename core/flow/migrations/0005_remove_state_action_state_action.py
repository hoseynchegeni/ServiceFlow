# Generated by Django 4.2.7 on 2023-12-16 07:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("flow", "0004_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="state",
            name="action",
        ),
        migrations.AddField(
            model_name="state",
            name="action",
            field=models.ManyToManyField(to="flow.action"),
        ),
    ]
