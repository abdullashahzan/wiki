from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path("wiki/", views.index, name="index"),
    path("wiki/<str:name>", views.openWtitle, name="openWtitle"),
    path("forms", views.bro, name="bro"),
    path("newpage", views.newpage, name="newpage"),
    path("saved", views.save, name="save"),
    path("edit/", views.edit, name="edit"),
    path("random", views.rand, name="random"),
    path("savenew", views.savenew, name='savenew')
]
