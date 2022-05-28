import imp
from django.urls import path
from . import views

app_name = "christmas"
urlpatterns = [
    path("", views.index, name="index")
]