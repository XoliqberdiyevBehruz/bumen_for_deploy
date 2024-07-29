# Generated by Django 5.0.6 on 2024-07-29 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0004_userotpcode"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userotpcode",
            name="is_active",
        ),
        migrations.AddField(
            model_name="userotpcode",
            name="is_used",
            field=models.BooleanField(default=False, verbose_name="is_active"),
        ),
    ]
