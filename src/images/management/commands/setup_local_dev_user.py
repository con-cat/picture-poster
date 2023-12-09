from django.conf import settings
from django.contrib.auth import models as auth_models
from django.core.management import base

USERNAME = "admin"
PASSWORD = "p"


class Command(base.BaseCommand):
    help = """Get or create a user for local development. If the user
    is newly-created, set some default values for them."""

    def handle(self, *args, **options):
        if not settings.DEBUG:
            raise base.CommandError("This command can only be run in debug mode.")

        user, created = auth_models.User.objects.get_or_create(username=USERNAME)
        if created:
            user.is_staff = True
            user.is_superuser = True
            user.set_password(PASSWORD)
            user.save()
