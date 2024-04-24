from django.shortcuts import render

def home(req):
    return render(req,"home.html")


def profile(req):
    return render(req,'profile.html')





