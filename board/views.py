from django.shortcuts import render
from django.http import HttpResponse

def create_board(request):
    return HttpResponse("get ready to create a board.")

def delete_board(request, id):
    return HttpResponse(f"the following board will be deleted {id}")

def update_board(request, id):
    return HttpResponse(f"the following board will be updated {id}")