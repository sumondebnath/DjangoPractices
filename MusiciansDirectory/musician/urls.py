from django.urls import path
from musician.views import addMusician, EditMusician

urlpatterns = [
    path("add/musician/", addMusician.as_view(), name="add_musician"),
    path("edit/<int:id>/", EditMusician.as_view(), name="edit_musician"),
]