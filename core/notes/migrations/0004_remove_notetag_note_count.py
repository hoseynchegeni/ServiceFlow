# Generated by Django 4.2.4 on 2023-10-24 06:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("notes", "0003_notetag_note_count"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="notetag",
            name="note_count",
        ),
    ]
