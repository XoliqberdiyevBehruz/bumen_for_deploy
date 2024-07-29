from django.contrib import admin

from .models import Groups, User, UserMessage


class UserMessageInlineAdmin(admin.StackedInline):
    model = UserMessage
    extra = 1


class UserAdmin(admin.ModelAdmin):
    inlines = [UserMessageInlineAdmin]


admin.site.register(User, UserAdmin)

admin.site.register(Groups)


class UserMessageAdmin(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


admin.site.register(UserMessage, UserMessageAdmin)
