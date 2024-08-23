

import company.validators
import django.db.models.deletion
import django_ckeditor_5.fields
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("common", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AboutMistake",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250, verbose_name="Name")),
                ("description", models.TextField(verbose_name="Description")),
                ("done", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "About Mistake",
                "verbose_name_plural": "About Mistakes",
            },
        ),
        migrations.CreateModel(
            name="AppInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=200, unique=True, verbose_name="Title"),
                ),
                ("description", models.TextField(verbose_name="Description")),
            ],
            options={
                "verbose_name": "App Info",
                "verbose_name_plural": "App Info",
            },
        ),
        migrations.CreateModel(
            name="Contacts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address", models.CharField(max_length=100)),
                (
                    "phone_number",
                    models.CharField(
                        max_length=100,
                        validators=[company.validators.phone_number_validator],
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("location", models.URLField()),
            ],
            options={
                "verbose_name": "Contacts",
            },
        ),
        migrations.CreateModel(
            name="ContactWithUs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                ("message", models.TextField()),
            ],
            options={
                "verbose_name": "Contact With Us",
                "verbose_name_plural": "Contact With Us",
            },
        ),
        migrations.CreateModel(
            name="ContactWithUsCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
            ],
            options={
                "verbose_name": "Contact With Us Category",
                "verbose_name_plural": "Contact With Us Category",
            },
        ),
        migrations.CreateModel(
            name="FAQ",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.TextField()),
                ("question_en", models.TextField(null=True)),
                ("question_uz", models.TextField(null=True)),
                ("question_ru", models.TextField(null=True)),
                ("answer", models.TextField()),
                ("answer_en", models.TextField(null=True)),
                ("answer_uz", models.TextField(null=True)),
                ("answer_ru", models.TextField(null=True)),
            ],
            options={
                "verbose_name": "FAQ",
            },
        ),
        migrations.CreateModel(
            name="PrivacyPolicy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", django_ckeditor_5.fields.CKEditor5Field(verbose_name="text")),
            ],
            options={
                "verbose_name": "Privacy Policy",
                "verbose_name_plural": "Privacy Policy",
            },
        ),
        migrations.CreateModel(
            name="SocialMedia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "telegram",
                    models.URLField(
                        validators=[company.validators.validate_telegram_url]
                    ),
                ),
                ("facebook", models.URLField()),
                (
                    "instagram",
                    models.URLField(
                        validators=[company.validators.validate_instagram_url]
                    ),
                ),
                ("linkedin", models.URLField()),
            ],
            options={
                "verbose_name": "Social Media",
                "verbose_name_plural": "Social Medias",
            },
        ),
        migrations.CreateModel(
            name="ContactWithUsReason",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contact_with_us_reasons",
                        to="company.contactwithuscategory",
                        verbose_name="Category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Contact With Us Reason",
                "verbose_name_plural": "Contact With Us Reason",
            },
        ),
        migrations.CreateModel(
            name="ContactWithUsMobile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="email")),
                ("message", models.TextField(verbose_name="text")),
                (
                    "file",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="common.media",
                        verbose_name="File",
                    ),
                ),
                (
                    "reason",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="company.contactwithusreason",
                        verbose_name="Reason",
                    ),
                ),
            ],
            options={
                "verbose_name": "Contact With Us Mobile",
                "verbose_name_plural": "Contact With Us Mobile",
            },
        ),
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50, verbose_name="title")),
                ("message", models.TextField(verbose_name="message")),
                (
                    "is_all_users",
                    models.BooleanField(default=False, verbose_name="is_all_users"),
                ),
                ("extra_data", models.JSONField(verbose_name="extra data")),
                (
                    "scheduled_date",
                    models.DateTimeField(blank=True, verbose_name="scheduled date"),
                ),
                ("users", models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "verbose_name": "Notification",
                "verbose_name_plural": "Notifications",
            },
        ),
        migrations.CreateModel(
            name="Sponsor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.URLField(verbose_name="URL")),
                (
                    "image",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="common.media",
                        verbose_name="Image",
                    ),
                ),
            ],
            options={
                "verbose_name": "Sponsor",
                "verbose_name_plural": "Sponsors",
            },
        ),
    ]
