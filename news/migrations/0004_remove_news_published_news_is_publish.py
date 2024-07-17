# Generated by Django 5.0.6 on 2024-07-10 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0003_news_published"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="news",
            name="published",
        ),
        migrations.AddField(
            model_name="news",
            name="is_publish",
            field=models.BooleanField(default=True, verbose_name="is publish"),
        ),
    ]
