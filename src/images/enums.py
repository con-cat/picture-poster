from django.db import models


class ThumbnailHeightChoices(models.IntegerChoices):
    """
    Possible heights for image thumbnails.
    """

    # I've chosen to define an enum of thumbnail size choices rather
    # than letting admins set arbitrary sizes so that thumbnails can
    # be shared between tiers, to reduce the number of new thumbnails
    # we'll need to generate when a user upgrades.
    H_100 = 100
    H_200 = 200
    H_300 = 300
    H_400 = 400
    H_500 = 500
    H_600 = 600
    H_700 = 700
    H_800 = 800
