from django.http import HttpResponse
from django.shortcuts import render

def app5home1(req):
    return HttpResponse("<h1>app5home1</h1>")

def app5home2(req):
    return HttpResponse("<h1>app5home2</h1>")

def app5home3(req):
    return HttpResponse("<h1>app5home3</h1>")

def app5home4(req):
    return HttpResponse("<h1>app5home4</h1>")

def app5home5(req):
    return HttpResponse("<h1>app5home5</h1>")
