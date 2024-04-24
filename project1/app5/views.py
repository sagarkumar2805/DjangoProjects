from django.shortcuts import render
from django.http import HttpResponse

def aap5home1(request):
    data = "<h1 style='color:red'>aap5home1</h1>"
    return HttpResponse(data)

def app5home2(request):
    data = "<h1 style='color:red'>aap5home2</h1>"
    return HttpResponse(data)

def app5home3(request):
    data = "<h1 style='color:red'>aap5home3</h1>"
    return HttpResponse(data)