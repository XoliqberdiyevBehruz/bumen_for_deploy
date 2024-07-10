from django.contrib import admin
from .models import Contacts, SocialMedia


# Register your models here.

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    pass


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    pass
