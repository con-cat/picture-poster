import io

from django.contrib.auth import models as auth_models
from easy_thumbnails import files as thumbnail_files

from . import models


def create_new_image_for_user(user: auth_models.User, image: io.BytesIO) -> models.Image:
    """
    Create a new Image instance for the user.
    """
    return models.Image.objects.create(original_file=image, user=user)


def get_thumbnnail_for_image(image: models.Image, height: int) -> thumbnail_files.ThumbnailFile:
    """
    Retrieve or generate a thumbnail for the image at the provided height.

    TODO: configure thumbnail options properly, e.g. cropping, image format, quality,
    etc. This currently returns a square JPEG image resized to fit within the height,
    preserving the aspect ratio.
    """
    thumbnailer = thumbnail_files.get_thumbnailer(image.original_file)
    return thumbnailer.get_thumbnail({"size": (height, height)})


def get_user_account_tier(user: auth_models.User) -> models.AccountTier:
    """
    Get the AccountTier associated with the user's account.
    """
    try:
        account = models.Account.objects.select_related("tier").get(user=user)
    except models.Account.DoesNotExist:
        raise ValueError("User is not associated with an account.")
    return account.tier
