# Generated by Django 4.2.7 on 2023-11-25 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("asset", "0010_licensecategory_license"),
    ]

    operations = [
        migrations.CreateModel(
            name="AccessoryCategory",
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
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Accessory",
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
                ("image", models.ImageField(blank=True, null=True, upload_to="images")),
                ("company", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=100)),
                ("model_number", models.CharField(max_length=100)),
                ("manufacturer", models.CharField(max_length=100)),
                ("supplier", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
                ("total", models.PositiveIntegerField(default=0)),
                ("available", models.PositiveIntegerField(default=0)),
                ("checked_out", models.PositiveIntegerField(default=0)),
                ("min_quantity", models.PositiveIntegerField(default=0)),
                ("purchase_date", models.DateField()),
                ("purchase_cost", models.DecimalField(decimal_places=2, max_digits=10)),
                ("order_number", models.CharField(max_length=100)),
                ("notes", models.TextField(blank=True)),
                ("in_out", models.CharField(max_length=10)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="asset.accessorycategory",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]