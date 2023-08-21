from django.urls import path

from . import views

urlpatterns = [
    path("", views.ListImages.as_view(), name="list-images"),
    path("create", views.CreateImage.as_view(), name="create-image"),
]
