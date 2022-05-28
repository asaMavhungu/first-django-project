from http.client import responses
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def asa(request):
    return HttpResponse("Hello ASA")

def greet(request, name : str):
    return render(request, "hello/greet.html", {
       "name": name.capitalize()
    })