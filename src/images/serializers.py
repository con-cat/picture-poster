from typing import Any

from rest_framework import serializers

from . import domain, models


class Image(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    original_file = serializers.ImageField()
    thumbnails = serializers.SerializerMethodField()

    def create(self, validated_data: dict[str, Any]) -> models.Image:
        original_file = validated_data["original_file"]
        user = self.context["request"].user
        return domain.create_new_image_for_user(user, original_file)

    def get_fields(self) -> dict[str, serializers.Field]:
        fields = super().get_fields()
        request = self.context["request"]
        account_tier = domain.get_user_account_tier(request.user)
        if request.method != "POST" and not account_tier.include_original_file:
            del fields["original_file"]
        return fields

    def get_thumbnails(self, image: models.Image) -> dict[int, str]:
        """
        Return a dictionary of thumbnail sizes and image URLs.

        Generates any thumbnails that haven't been created yet.
        """
        account_tier = domain.get_user_account_tier(image.user)
        request = self.context["request"]
        return {
            height: request.build_absolute_uri(domain.get_thumbnnail_for_image(image, height).url)
            for height in account_tier.thumbnail_sizes
        }
