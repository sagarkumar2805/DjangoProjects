from django.shortcuts import render
from django.http import HttpResponse

def aap3home1(request):
    data = "<h1 style='color:red'>aap3home1</h1>"
    return HttpResponse(data)

def app3home2(request):
    data = "<h1 style='color:red'>aap3home2</h1>"
    return HttpResponse(data)

def app3home3(request):
    data = "<h1 style='color:red'>aap3home3</h1>"
    return HttpResponse(data)