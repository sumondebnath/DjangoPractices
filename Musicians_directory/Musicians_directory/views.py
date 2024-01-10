from django.shortcuts import render, redirect
from musician import forms, models
from album import models

def home(request):
    data = models.Albums.objects.all()
    return render(request, "home.html", {"data":data})
