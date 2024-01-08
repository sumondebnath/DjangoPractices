from django.shortcuts import render
from formAPI.forms import djangoFormApi

# Create your views here.
def home(request):
    form = djangoFormApi()
    return render(request, "formAPI/home.html", {"form":form})
