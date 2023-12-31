from django.shortcuts import render
from django.http import HttpResponse


def delete_creator(request, id):
    return HttpResponse(f"the following creator will be deleted {id}")

def update_profile(request, id):
    return HttpResponse(f"the following creator will be updated {id}")
