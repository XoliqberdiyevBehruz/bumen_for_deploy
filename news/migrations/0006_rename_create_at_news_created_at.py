# Generated by Django 5.0.6 on 2024-07-12 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0005_alter_news_managers"),
    ]

    operations = [
        migrations.RenameField(
            model_name="news",
            old_name="create_at",
            new_name="created_at",
        ),
    ]
