# Generated by Django 5.0.6 on 2024-08-12 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("supject", "0003_usersubject_started_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usersubject",
            name="total_test_ball",
            field=models.PositiveIntegerField(
                default=0.0, verbose_name="Total test bal"
            ),
        ),
    ]
