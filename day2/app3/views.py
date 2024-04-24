from django.http import HttpResponse
from django.shortcuts import render

def app3home1(req):
    return HttpResponse("<h1>app3home1</h1>")

def app3home2(req):
    return HttpResponse("<h1>app3home2</h1>")

def app3home3(req):
    return HttpResponse("<h1>app3home3</h1>")

def app3home4(req):
    return HttpResponse("<h1>app3home4</h1>")

def app3home5(req):
    return HttpResponse("<h1>app3home5</h1>")
