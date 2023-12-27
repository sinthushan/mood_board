from django.urls import path

from . import views

urlpatterns = [
    path("create", views.create_board, name="create_board"),
    path("/<int:id>/delete", views.delete_board, name="delete_board"),
    path("/<int:id>/update", views.update_board, name="update+_board"),
]

