from django import test
from django.urls import reverse

from tests import factories


class TestListImages:
    def test_requires_authentication(self):
        client = test.Client()
        response = client.get(reverse("list-images"))
        breakpoint()

    def test_lists_images(self):
        pass

    def test_respects_account_tier(self):
        pass


class TestCreateImage:
    def test_requires_authentication(self):
        pass

    def test_can_create_image(self):
        pass
