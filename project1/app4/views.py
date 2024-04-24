from django.shortcuts import render
from django.http import HttpResponse

def aap4home1(request):
    data = "<h1 style='color:red'>aap4home1</h1>"
    return HttpResponse(data)

def app4home2(request):
    data = "<h1 style='color:red'>aap4home2</h1>"
    return HttpResponse(data)

def app4home3(request):
    data = "<h1 style='color:red'>aap4home3</h1>"
    return HttpResponse(data)