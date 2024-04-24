from django.http import HttpResponse
from django.shortcuts import render

def app4home1(req):
    return HttpResponse("<h1>app4home1</h1>")

def app4home2(req):
    return HttpResponse("<h1>app4home2</h1>")

def app4home3(req):
    return HttpResponse("<h1>app4home3</h1>")

def app4home4(req):
    return HttpResponse("<h1>app4home4</h1>")

def app4home5(req):
    return HttpResponse("<h1>app4home5</h1>")
