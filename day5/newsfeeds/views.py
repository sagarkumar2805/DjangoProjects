from django.shortcuts import render

def news(request):
    return render(request,"index.html")

def movies(request):
    return render(request,"movies.html")

def sports(request):
    return render(request,"sports.html")

def politics(request):
    return render(request,"politics.html")
