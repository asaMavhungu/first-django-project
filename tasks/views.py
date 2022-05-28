from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse(f"Hello there")


def greet(request, name:str):
    return render(request, "tasks/index.html", {
        "name" : name 
    })