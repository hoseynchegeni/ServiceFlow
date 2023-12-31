# Generated by Django 4.2.6 on 2023-11-01 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("department", "0001_initial"),
        ("team", "0008_remove_team_department"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="department",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="department",
                to="department.department",
            ),
        ),
    ]
