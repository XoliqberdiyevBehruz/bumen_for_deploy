from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("supject", "0002_alter_category_click_count"),

        ("supject", "0002_alter_usersubject_total_test_ball"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="click_count",
            field=models.PositiveIntegerField(default=0, verbose_name="Click Count"),
        ),
    ]
