# Generated by Django 4.2.7 on 2023-12-07 09:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("organization", "0007_alter_organization_logo"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="organization",
            name="org",
        ),
    ]
