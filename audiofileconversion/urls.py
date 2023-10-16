from django.urls import path
from . import views

urlpatters = [
    path("", view.index, name="index")
]