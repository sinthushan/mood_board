from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm
from .models import Gallery
from creator.models import Creator
from django.contrib.auth.decorators import login_required

@login_required
def gallery(request, id):
    creator = request.user.creator
    images = creator.gallery.get_image_urls
    return render(request, "creator/gallery/gallery.html", {"images": images, "creator_id": creator.id})

@login_required
def upload_image(request, id):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            creator = request.user.creator
            gallery = creator.gallery
            gallery.upload_img(request.FILES['file'])
            return HttpResponseRedirect(f"/creator/{id}/gallery")
    else:
        form = UploadFileForm()
    return render(request, f"creator/gallery/upload.html", {"form": form})

def view_image(request, id, image_id):
    return HttpResponse(f"the following user {id} has uploaded the following image {image_id}")

