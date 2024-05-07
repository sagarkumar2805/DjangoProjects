from django.shortcuts import render

def app1Home(req):
    return render(req,"home.html")


def app1Profile(req):
    return render(req,'profile.html')





