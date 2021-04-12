from django.shortcuts import render
from django.http import HttpResponse

def view1(request):
    return HttpResponse("<h1> hii...hello</h1>")


def view2(request,email):
    return render(request,"view2.html",context={'email':email,'name':"Kavya"})

def view3(request,name):
    return HttpResponse(f'<h1>hello Mr/miss {name}</h1>')

# Create your views here.
