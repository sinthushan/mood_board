from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def create_board(request):
    print(request.User)
    return render(request, "board/create.html", )

def delete_board(request, id):
    return HttpResponse(f"the following board will be deleted {id}")

def update_board(request, id):
    return HttpResponse(f"the following board will be updated {id}")