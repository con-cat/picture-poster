import json

import pytest
from django.urls import reverse
from images import models

from . import factories

# TODO: I have provided some basic end-to-end tests here asserting that the views
# require authentication and the responses have the expected shape. Given more time I
# would have written more tests, and the majority of tests would be more granular unit
# or integration tests of individual functions and methods.


class TestListImages:
    def test_requires_authentication(self, client):
        response = client.get(reverse("list-images"))

        assert response.status_code == 403

    @pytest.mark.django_db()
    def test_lists_images(self, client):
        basic_account_tier = models.AccountTier.objects.get(name="Basic")
        account = factories.Account(tier=basic_account_tier)
        num_images = 2
        for _ in range(num_images):
            factories.Image(user=account.user)
        client.login(username="user", password="secret_password")

        response = client.get(reverse("list-images"))
        content = json.loads(response.content)
        results = content.get("results")

        assert response.status_code == 200
        assert len(results) == num_images

    @pytest.mark.django_db()
    @pytest.mark.parametrize(
        "tier_name,expected_sizes,includes_original",
        [
            ("Basic", ["200"], False),
            ("Premium", ["200", "400"], True),
            ("Enterprise", ["200", "400"], True),
        ],
    )
    def test_respects_account_tier(self, client, tier_name, expected_sizes, includes_original):
        account_tier = models.AccountTier.objects.get(name=tier_name)
        account = factories.Account(tier=account_tier)
        factories.Image(user=account.user)
        client.login(username="user", password="secret_password")

        response = client.get(reverse("list-images"))
        content = json.loads(response.content)
        results = content.get("results")

        assert response.status_code == 200
        assert len(results) == 1
        result = results[0]
        assert list(result["thumbnails"].keys()) == expected_sizes
        has_original_file = result.get("original_file") is not None
        assert has_original_file == includes_original


class TestCreateImage:
    def test_requires_authentication(self, client):
        response = client.get(reverse("create-image"))

        assert response.status_code == 403
