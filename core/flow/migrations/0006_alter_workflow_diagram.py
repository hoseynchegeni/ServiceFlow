# Generated by Django 4.2.8 on 2023-12-16 08:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("flow", "0005_remove_state_action_state_action"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workflow",
            name="diagram",
            field=models.ImageField(blank=True, null=True, upload_to="images"),
        ),
    ]
