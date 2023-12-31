# Generated by Django 4.2.6 on 2023-11-01 11:36

import department.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("organization", "0006_delete_department"),
    ]

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "org",
                    models.CharField(
                        default=department.models.generate_pk,
                        editable=False,
                        max_length=255,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("active_status", models.BooleanField(default=True)),
                (
                    "manager",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="organization.organization",
                    ),
                ),
            ],
        ),
    ]
