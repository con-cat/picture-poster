from django.db import models as django_models
from django.shortcuts import render
from rest_framework import generics, pagination, permissions

from . import models, serializers


class CreateImage(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.Image


class ImagePagination(pagination.CursorPagination):
    page_size = 100
    ordering = "-created_at"


class ListImages(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.Image
    pagination_class = ImagePagination

    def get_queryset(self) -> django_models.QuerySet[models.Image]:
        return models.Image.objects.filter(user=self.request.user).select_related(
            "user", "user__account", "user__account__tier"
        )
