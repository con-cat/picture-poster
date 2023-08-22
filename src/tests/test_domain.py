from unittest import mock

import pytest
from images import domain, models

from . import factories


@pytest.mark.django_db()
class TestCreateDisappearingLink:
    def test_creates_unique_records_for_same_image(self):
        image = factories.Image()
        seconds_valid = 300
        num_links = 3

        for _ in range(num_links):
            domain.create_disappearing_link(image, seconds_valid)

        disappearing_links = models.DisappearingLink.objects.filter(image=image, seconds_valid=300)
        assert disappearing_links.exists()
        assert disappearing_links.count() == num_links


@pytest.mark.django_db()
class TestGetUniqueDisappearingLinkSlug:
    def test_returns_6_character_path(self):
        result = domain.get_unique_disappearing_link_slug()

        assert len(result) == 6

    @mock.patch("django.utils.crypto.get_random_string", side_effect=["abc123", "abc124"])
    def test_handles_collisions_with_existing_urls(self, mock_get_random_string):
        # Create an existing DisappearingLink with a slug that matches the
        # first result from the mocked get_random_string
        factories.DisappearingLink(slug="abc123")

        result = domain.get_unique_disappearing_link_slug()

        assert result == "abc124"
        assert mock_get_random_string.call_count == 2
