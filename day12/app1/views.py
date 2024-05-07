from django.shortcuts import render

def home(request):
    return render(request,'app1/home.html')

def login(request):
    return render(request,'app1/login.html')

def register(request):
    return render(request,'app1/register.html')
