# Generated by Django 4.2.14 on 2024-08-16 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0007_alter_news_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="news",
            name="description_en",
        ),
        migrations.RemoveField(
            model_name="news",
            name="description_ru",
        ),
        migrations.RemoveField(
            model_name="news",
            name="description_uz",
        ),
        migrations.RemoveField(
            model_name="news",
            name="title_en",
        ),
        migrations.RemoveField(
            model_name="news",
            name="title_ru",
        ),
        migrations.RemoveField(
            model_name="news",
            name="title_uz",
        ),
    ]
