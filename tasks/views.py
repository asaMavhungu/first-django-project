from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

tasks = ["foo", "bar", "faz"]

def index(request):
    return render(request, "tasks/index.html", {
        "tasks" : tasks
    })