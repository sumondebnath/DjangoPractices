from django.shortcuts import render,redirect
from musician.forms import musicianForm
from musician.models import Musician
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
class addMusician(CreateView):
    model = Musician
    form_class = musicianForm
    template_name = "musicians.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        return super().form_valid(form)
    
class EditMusician(UpdateView):
    model = Musician
    form_class = musicianForm
    template_name = "musicians.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("home")


# def addMusician(request):
#     return render(request, "musicians.html")