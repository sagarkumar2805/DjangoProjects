from django.shortcuts import render
from django.http import HttpResponse

def aap2home1(request):
    data = "<h1 style='color:red'>aap2home1</h1>"
    return HttpResponse(data)

def app2home2(request):
    data = "<h1 style='color:red'>aap2home2</h1>"
    return HttpResponse(data)

def app2home3(request):
    data = "<h1 style='color:red'>aap2home3</h1>"
    return HttpResponse(data)

# Create your views here.
