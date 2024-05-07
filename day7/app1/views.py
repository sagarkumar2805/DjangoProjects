from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def resume(request):
    return render(request,'resume.html')

def contact(request):
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')

def portfolio(request):
    return render(request,'portfolio.html')


# def abc(request):
#     return render(request,'abc.html')

# Create your views here.
