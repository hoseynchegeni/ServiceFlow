# Generated by Django 4.2.7 on 2023-12-07 09:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("notes", "0012_alter_note_tags"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="note",
            name="note",
        ),
    ]
