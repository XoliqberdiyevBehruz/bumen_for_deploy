# Generated by Django 5.0.6 on 2024-08-19 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0003_user_telegram_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="device_id",
            field=models.CharField(
                default=1, max_length=244, unique=True, verbose_name="device id"
            ),
            preserve_default=False,
        ),
    ]
