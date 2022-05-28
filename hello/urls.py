from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name = "index"),
    path("asa", views.asa, name = "asa"),
    path("<str:name>", views.greet, name = "greet")
]