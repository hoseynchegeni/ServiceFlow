# Generated by Django 4.2.6 on 2023-11-08 15:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0013_article_is_checked"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="article",
            name="is_checked",
        ),
    ]