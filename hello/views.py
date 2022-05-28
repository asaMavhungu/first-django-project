from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello world!!!!")

def asa(request):
    return HttpResponse("Hello ASA")

def greet(request, name):
    return HttpResponse(f"Hello, {name}!")