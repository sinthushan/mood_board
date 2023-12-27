from django.urls import path

from . import views

urlpatterns = [
    path("/<int:id>/delete", views.delete_creator, name="delete_creator"),
    path("/<int:id>/update", views.update_profile, name="update_profile"),
]
