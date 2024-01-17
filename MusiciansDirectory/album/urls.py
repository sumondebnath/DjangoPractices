from django.urls import path
from album.views import addAlbum,DeleteAll, EditAlbum, Home

urlpatterns = [
    path("add/album/", addAlbum.as_view(), name="add_album"),
    path("delete/<int:id>/", DeleteAll.as_view(), name="delete"),
    path("edit/<int:id>/", EditAlbum.as_view(), name="edit_album"),
    path("", Home, name="home"),
]