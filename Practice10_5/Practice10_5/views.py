
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    dict = {"srcOne": "https://www.geeksforgeeks.org/django-template-filters/", "srcTwo": "https://earthly.dev/blog/django-template-filters/"}
    
    return render(request,"home.html", dict)