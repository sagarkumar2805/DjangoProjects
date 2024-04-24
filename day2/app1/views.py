from django.http import HttpResponse
from django.shortcuts import render

def app1home1(req):
    return HttpResponse("<h1>app1home1</h1>")

def app1home2(req):
    return HttpResponse("<h1>app1home2</h1>")

def app1home3(req):
    return HttpResponse("<h1>app1home3</h1>")

def app1home4(req):
    return HttpResponse("<h1>app1home4</h1>")

def app1home5(req):
    return HttpResponse("<h1>app1home5</h1>")
