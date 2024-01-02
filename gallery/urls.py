from django.urls import path, include

from . import views

urlpatterns = [
    path("image/upload", views.upload_image, name="upload"),
    path("image/<int:image_id>", views.view_image, name="view_image"),
    path("", views.gallery, name="gallery")
]