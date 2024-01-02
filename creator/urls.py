from django.urls import path, include

from . import views

urlpatterns = [
    path("<int:id>/delete", views.delete_creator, name="delete_creator"),
    path("<int:id>/update", views.update_profile, name="update_profile"),
    path("<int:id>", views.profile, name="profile"),
    path("<int:id>/gallery/", include('gallery.urls'))
]
