from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm
from .models import Gallery
from creator.models import Creator
from django.contrib.auth.decorators import login_required

def gallery(request, id):
    return HttpResponse(f"this gallery belongs to user {id}")

@login_required
def upload_image(request, id):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            creator =  Creator.objects.get(pk=id)
            gallery = creator.gallery
            gallery.upload_img(request.FILES['file'])
            return HttpResponseRedirect(f"/creator/{id}")
    else:
        form = UploadFileForm()

    return render(request, "creator/gallery/upload.html", {"form": form})

def view_image(request, id, image_id):
    return HttpResponse(f"the following user {id} has uploaded the following image {image_id}")

