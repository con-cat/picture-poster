import factory
from django.conf import settings
from django.contrib.auth import models as auth_models
from images import models

FIXTURE_PATH = settings.BASE_DIR / "tests/fixtures/"
IMAGE_FIXTURE_PATH = FIXTURE_PATH / "geese.jpg"


class User(factory.django.DjangoModelFactory):
    username = factory.LazyAttribute(lambda _: "user")
    password = factory.PostGenerationMethodCall("set_password", "secret_password")

    class Meta:
        model = auth_models.User


class Account(factory.django.DjangoModelFactory):
    user = factory.SubFactory(User)

    class Meta:
        model = models.Account


class Image(factory.django.DjangoModelFactory):
    original_file = factory.django.ImageField(from_path=IMAGE_FIXTURE_PATH)
    user = factory.SubFactory(User)

    class Meta:
        model = models.Image
