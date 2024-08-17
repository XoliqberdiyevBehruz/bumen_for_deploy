# Generated by Django 5.1 on 2024-08-17 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0009_user_auth_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="socialuser",
            name="provider",
            field=models.CharField(
                choices=[
                    ("google", "google"),
                    ("facebook", "facebook"),
                    ("telegram", "telegram"),
                ],
                max_length=255,
                verbose_name="provider",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="auth_type",
            field=models.CharField(
                choices=[
                    ("GOOGLE", "Google Account"),
                    ("FACEBOOK", "Facebook Account"),
                    ("TELEGRAM", "Telegram Account"),
                    ("WITH EMAIL", "Email Account"),
                ],
                max_length=244,
                verbose_name="auth type",
            ),
        ),
    ]
