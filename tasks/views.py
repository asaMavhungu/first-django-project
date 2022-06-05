from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse

# Create your views here.

tasks = []

class simpleForm(forms.Form):
    task = forms.CharField(label="task")
    priority = forms.IntegerField(label="priority", min_value=0, max_value= 10)

def index(request):
    return render(request, "tasks/index.html", {
        "tasks" : tasks
    })

def add(request):
    if request.method == "POST":
        form = simpleForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
            "form": form
        })
    return render(request, "tasks/add.html", {
        "form": simpleForm
    })