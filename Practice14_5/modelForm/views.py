from django.shortcuts import render
from modelForm.forms import allForms

# Create your views here.
def allForm(request):
    form = allForms
    return render(request, "modelForm/modelfm.html", {"form":form})