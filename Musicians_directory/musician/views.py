from django.shortcuts import render, redirect
from musician.forms import musiciansForm
from musician.models import Musicians
# Create your views here.
def addMusicians(request):
    if request.method == "POST":
        form = musiciansForm(request.POST)
        if form.is_valid():
            form.save()
            # print(request.POST)
            return redirect("add_musician")
    else:
        form = musiciansForm()
    return render(request, "musician/addMusician.html", {"form":form})

def editMusician(request, id):
    info = Musicians.objects.get(pk=id)
    form = musiciansForm(instance=info)
    if request.method == "POST":
        form = musiciansForm(request.POST, instance=info)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request, "musician/addMusician.html", {"form":form})

def allDelete(request, id):
    del_item = Musicians.objects.get(pk=id)
    del_item.delete()
    return redirect("home")