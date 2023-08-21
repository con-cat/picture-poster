from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from images import models


class AccountInline(admin.StackedInline):
    model = models.Account
    can_delete = False
    verbose_name_plural = "account"


class UserAdmin(BaseUserAdmin):
    """
    Custom User admin with Account model fields inline.
    """

    inlines = [AccountInline]


admin.site.register(models.AccountTier)
admin.site.register(models.Image)
# Re-register UserAdmin with AccountInline
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
