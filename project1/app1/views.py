from django.shortcuts import render
from django.http import HttpResponse

def aap1home1(request):
    data = "<h1 style='color:red'>aap1home1</h1>"
    return HttpResponse(data)

def app1home2(request):
    data = "<h1 style='color:red'>aap1home2</h1>"
    return HttpResponse(data)

def app1home3(request):
    data = "<h1 style='color:red'>aap1home3</h1>"
    return HttpResponse(data)

# Create your views here.
