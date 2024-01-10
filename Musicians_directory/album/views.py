from django.shortcuts import render, redirect
from album.forms import albumForm
from album.models import Albums

# Create your views here.
def AddAlbums(request):
    if request.method == "POST":
        form = albumForm(request.POST)
        if form.is_valid():
            form.save()
            # print(request.POST)
            return redirect("add_album")
    else:
        form = albumForm()
    return render(request, "album/Album.html", {"form":form})

def editAlbum(request, id):
    info = Albums.objects.get(pk=id)
    form = albumForm(instance=info)
    if request.method == "POST":
        form = albumForm(request.POST, instance=info)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request, "album/Album.html", {"form":form})

