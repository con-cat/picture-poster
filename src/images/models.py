from django.contrib.auth import models as auth_models
from django.contrib.postgres import fields as postgres_fields
from django.db import models

from . import enums


class AccountTier(models.Model):
    name = models.CharField(unique=True)
    thumbnail_sizes = postgres_fields.ArrayField(
        models.IntegerField(choices=enums.ThumbnailHeightChoices.choices)
    )
    include_original_file = models.BooleanField(default=False)
    can_generate_expiring_links = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class Account(models.Model):
    user = models.OneToOneField(auth_models.User, related_name="account", on_delete=models.CASCADE)
    tier = models.ForeignKey(AccountTier, related_name="accounts", on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"Username: {self.user}, tier: {self.tier}"


class Image(models.Model):
    original_file = models.ImageField()
    user = models.ForeignKey(auth_models.User, related_name="images", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.original_file)


class DisappearingLink(models.Model):
    image = models.ForeignKey(Image, related_name="disappearing_links", on_delete=models.CASCADE)
    slug = models.SlugField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    seconds_valid = models.IntegerField()
