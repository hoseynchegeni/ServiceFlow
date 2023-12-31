# Generated by Django 4.2.6 on 2023-10-29 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("team", "0003_remove_team_members"),
        ("accounts", "0004_alter_user_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="member_of",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="member",
                to="team.team",
            ),
        ),
    ]
