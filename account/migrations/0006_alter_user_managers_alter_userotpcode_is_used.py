# Generated by Django 5.0.6 on 2024-08-02 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0005_remove_userotpcode_is_active_userotpcode_is_used"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[],
        ),
        migrations.AlterField(
            model_name="userotpcode",
            name="is_used",
            field=models.BooleanField(default=False, verbose_name="is_used"),
        ),
    ]
