# Generated by Django 4.2.8 on 2023-12-16 14:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0024_tasklogflow"),
    ]

    operations = [
        migrations.AddField(
            model_name="tasklogflow",
            name="attachments_1",
            field=models.FileField(blank=True, null=True, upload_to="attachments"),
        ),
        migrations.AddField(
            model_name="tasklogflow",
            name="attachments_2",
            field=models.FileField(blank=True, null=True, upload_to="attachments"),
        ),
        migrations.AddField(
            model_name="tasklogflow",
            name="attachments_3",
            field=models.FileField(blank=True, null=True, upload_to="attachments"),
        ),
        migrations.AddField(
            model_name="tasklogflow",
            name="comment",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="tasklogflow",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(
                    2023, 12, 16, 14, 4, 39, 137858, tzinfo=datetime.timezone.utc
                ),
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="tasklogflow",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]
