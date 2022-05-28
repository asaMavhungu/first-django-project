from django.http import HttpResponse
from django.shortcuts import render
from requests import request
import datetime
# Create your views here.
def index(request):
    now = datetime.datetime.now()
    #return HttpResponse("Hello There")
    return render(request, "christmas/index.html", {
        "christmas" : now.month == 12 and now.day == 25
    })