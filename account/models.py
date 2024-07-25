from django.contrib.auth.models import AbstractUser
from django.db import models

from common.models import Media


class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    photo = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)
