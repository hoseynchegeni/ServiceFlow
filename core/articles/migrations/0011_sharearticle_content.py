# Generated by Django 4.2.6 on 2023-11-06 08:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0010_alter_commentsharearticle_share_article"),
    ]

    operations = [
        migrations.AddField(
            model_name="sharearticle",
            name="content",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]