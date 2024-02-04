from django.shortcuts import render
import os
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from creator.models import Creator


@login_required(login_url='/creator/login')
def create_board(request):
    user_id = request.user.id
    creator =  Creator.objects.get(user_id=user_id)
    gallery = creator.gallery
    
    inspos = gallery.inspo_set.all()
    images = ['../' + inspo.image_url for inspo in inspos]

    return render(request, "board/create.html", {"images": images})

@login_required(login_url='/creator/login')
def get_boards(request):
    user_id = request.user.id
    creator =  Creator.objects.get(user_id=user_id)
    boards = creator.board_set.all()
    return render(request, "board/all.html", {"boards": boards})

@login_required(login_url='/creator/login')
def delete_board(request, id):
    return HttpResponse(f"the following board will be deleted {id}")


@login_required(login_url='/creator/login')
def update_board(request, id):
    return HttpResponse(f"the following board will be updated {id}")