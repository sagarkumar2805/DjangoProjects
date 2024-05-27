from django.shortcuts import render
from .models import *

def studentData(request):
    data = Student.objects.all()

    return render(request,'index.html',context={'data':data})

