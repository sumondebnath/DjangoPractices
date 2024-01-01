from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
    d = {"lst":[10, 20, 30, 40], "str":["sumon", "deb", "nath", "manu"], "val":25,
         "list" :[
             {
                 "name":"Sumon Debnath",
                 "age" : 25,
                 "gender" : "male" 
             },
             {
                 "name": "Ami Manu",
                 "age": 21,
                 "gender": "male"
             },
             {
                 "name": "Unknown",
                 "age": 31,
                 "gender": "undefined"
             }
         ],
        }
    return render(request, "navContext/home.html", context=d)

def about(request):
    dic = {"str": "my name is Sumon Debnath, i am from jashore. Right now i am nobody.", "publish":datetime.datetime.now(), "publishDate": "jan-1-23",
            "val" : "sumon debnath",   
        }

    return render(request, "navContext/about.html", dic)

def contact(request):
    d = {"val": "sumon debnath manu", "var" : 123456789, "emp":" ",}

    return render(request, "navContext/contact.html", d)