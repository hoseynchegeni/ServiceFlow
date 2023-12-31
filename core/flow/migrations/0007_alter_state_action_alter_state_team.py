# Generated by Django 4.2.8 on 2023-12-17 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("team", "0011_remove_team_team"),
        ("flow", "0006_alter_workflow_diagram"),
    ]

    operations = [
        migrations.AlterField(
            model_name="state",
            name="action",
            field=models.ManyToManyField(blank=True, to="flow.action"),
        ),
        migrations.AlterField(
            model_name="state",
            name="team",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="team.team",
            ),
        ),
    ]
