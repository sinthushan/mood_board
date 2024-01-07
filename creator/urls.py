from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path("sucess", views.sucess, name="sucess"),
    path("login", LoginView.as_view(template_name="creator/login.html", next_page="sucess"), name="login"),
    path("<int:id>/delete", views.delete_creator, name="delete_creator"),
    path("<int:id>/update", views.update_profile, name="update_profile"),
    path("<int:id>", views.profile, name="profile"),
    path("<int:id>/gallery/", include('gallery.urls'))
    
]
