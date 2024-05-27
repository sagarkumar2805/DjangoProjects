from django.shortcuts import render
from .models import *

def bookData(request):
    data = Book.objects.all()
    
    return render(request,'index.html',context={'data':data})