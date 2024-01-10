from django.urls import path
from musician.views import addMusicians, editMusician, allDelete

urlpatterns = [
    path("add/", addMusicians, name="add_musician"),
    path("edit/musician/<int:id>",editMusician, name="edit_musician"),
    path("delete/<int:id>", allDelete, name="delete"),
]