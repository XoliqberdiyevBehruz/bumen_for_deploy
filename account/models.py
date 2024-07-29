from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import Media


class User(AbstractUser):
    birth_date = models.DateField(_("birth_date"), null=True, blank=True)
    photo = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")


class UserOtpCode(models.Model):
    class VerificationType(models.TextChoices):
        REGISTER = "register"
        RESET_PASSWORD = "reset_password"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    type = models.CharField(_("type"), max_length=20, choices=VerificationType.choices)
    expires_in = models.DateTimeField(_("expires_in"), null=True, blank=True)
    is_used = models.BooleanField(_("is_used"), default=False)

    def __str__(self) -> str:
        return self.code


class Groups(models.Model):
    name = models.CharField(_("name"), max_length=100)
    users = models.ManyToManyField(User, related_name="user_groups")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Group")
        verbose_name_plural = _("Groups")


class UserMessage(models.Model):
    user = models.ForeignKey(verbose_name=_("User"), to=User, on_delete=models.CASCADE)
    message = models.TextField(verbose_name=_("Message"))
    file = models.OneToOneField(
        verbose_name=_("File"),
        to=Media,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    group = models.ForeignKey(
        verbose_name=_("Group"), to=Groups, on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"{self.user.username} - {self.group.name}"

    class Meta:
        verbose_name = _("User's message")
        verbose_name_plural = _("User's messages")
