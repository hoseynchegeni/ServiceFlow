# Generated by Django 4.2.6 on 2023-11-08 14:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0012_article_is_approved"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="is_checked",
            field=models.BooleanField(default=False),
        ),
    ]