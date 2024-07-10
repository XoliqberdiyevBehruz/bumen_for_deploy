from django.contrib import admin
from .models import Media

from django.contrib.auth.models import User, Group

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    pass


