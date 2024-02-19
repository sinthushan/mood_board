from django.shortcuts import render
import os
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from creator.models import Creator


@login_required(login_url='/creator/login')
def create_board(request):
    creator = request.user.creator
    images = creator.gallery.get_image_urls

    return render(request, "board/create.html", {"images": images, "creator_id": creator.id})

@login_required(login_url='/creator/login')
def get_boards(request):
    creator = request.user.creator
    boards = creator.board_set.all()
    return render(request, "board/all.html", {"boards": boards, "creator_id": creator.id})

@login_required(login_url='/creator/login')
def delete_board(request, id):
    return HttpResponse(f"the following board will be deleted {id}")


@login_required(login_url='/creator/login')
def update_board(request, id):
    return HttpResponse(f"the following board will be updated {id}")