# Generated by Django 4.2.6 on 2023-11-16 13:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("asset", "0004_rename_asetstatus_assetstatus"),
    ]

    operations = [
        migrations.RenameField(
            model_name="asset",
            old_name="asset_name",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="asset",
            old_name="asset_type",
            new_name="type",
        ),
    ]