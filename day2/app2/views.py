from django.http import HttpResponse
from django.shortcuts import render

def app2home1(req):
    return HttpResponse("<h1>app2home1</h1>")

def app2home2(req):
    return HttpResponse("<h1>app2home2</h1>")

def app2home3(req):
    return HttpResponse("<h1>app2home3</h1>")

def app2home4(req):
    return HttpResponse("<h1>app2home4</h1>")

def app2home5(req):
    return HttpResponse("<h1>app2home5</h1>")
