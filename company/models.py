from django.db import models
from .validators import phone_number_validator, validate_instagram_url, validate_telegram_url
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Contacts(models.Model):
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, validators=[phone_number_validator])
    email = models.EmailField()
    location = models.URLField()

    class Meta:
        verbose_name = "Contacts"


class SocialMedia(models.Model):
    telegram = models.URLField(validators=[validate_telegram_url])
    facebook = models.URLField(validators=[])
    instagram = models.URLField(validators=[validate_instagram_url])
    linkedin = models.URLField(validators=[])

    class Meta:
        verbose_name = "Social Media"
        verbose_name_plural = "Social Medias"


class ContactWithUs(models.Model):
    name = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    message = models.TextField()

    class Meta:
        verbose_name = _("Contact With Us")
        verbose_name_plural = _("Contact With Us")


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    class Meta:
        verbose_name = "FAQ"

