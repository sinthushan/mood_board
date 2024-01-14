from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Register
from .models import User, Creator
from gallery.models import Gallery

def register(request):
    err_msg = ""
    if request.method == "POST":
        form = Register(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        if password !=  confirm_password:
            form = Register()
            err_msg = "Mismatching password"
            return render(request, "creator/register.html", {"form": form, "err_msg":err_msg})
        if form.is_valid():
            user = User.objects.create_user(username, password=password)
            user.save()
            creator = Creator(user=user)
            creator.save()
            id = creator.id
            gallery = Gallery(creator=creator)
            gallery.save()
            return HttpResponseRedirect(f"/creator/{id}")
    else:
        form = Register()
        return render(request, "creator/register.html", {"form": form, "err_msg":err_msg})

def sucess(request):
    id = request.user.id
    return HttpResponseRedirect(f"/creator/{id}")

def profile(request, id):
    return HttpResponse(f"welcome to your profile {id}")

def delete_creator(request, id):
    return HttpResponse(f"the following creator will be deleted {id}")

def update_profile(request, id):
    return HttpResponse(f"the following creator will be updated {id}")
