from django.shortcuts import render

def app2Home(req):
    return render(req, "home.html")

def app2Profile(req):
    return render(req,"profile.html")
