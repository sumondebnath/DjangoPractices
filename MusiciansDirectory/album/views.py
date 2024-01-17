from django.shortcuts import render
from album.forms import albumForm
from album.models import Album
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy

# Create your views here.
class addAlbum(CreateView):
    model = Album
    form_class = albumForm
    template_name = "albums.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        return super().form_valid(form)
    
class EditAlbum(UpdateView):
    model = Album
    form_class = albumForm
    template_name = "albums.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("home")

class DeleteAll(DeleteView):
    model = Album
    template_name = "home.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("home")

# class Home(DetailView):
#     model = Album
#     pk_url_kwarg = "id"
#     template_name = "home.html"
    
def Home(request):
    form = Album.objects.all()
    return render(request, "home.html", {"form":form})