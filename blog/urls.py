from django.urls import path, re_path
from . import views

urlpatterns = [
    path(route="", view=views.index, name="index"),
]
