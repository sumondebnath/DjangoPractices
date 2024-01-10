from django.urls import path
from album.views import AddAlbums, editAlbum

urlpatterns = [
    path("add/", AddAlbums, name="add_album"),
    path("edit/album/<int:id>", editAlbum, name="edit_album"),
]