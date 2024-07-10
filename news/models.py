from django.db import models
from common.models import Media
from django.utils.translation import gettext_lazy as _
from .managers import NewsManager


# Create your models here.
class News(models.Model):
    image = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True)
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'))
    create_at = models.DateTimeField(_('create at'), auto_now_add=True)
    is_publish = models.BooleanField(_('is publish'), default=True)
    published = NewsManager()

    class Meta:
        verbose_name = _('news')
        verbose_name_plural = _('news')

    def __str__(self):
        return self.title
