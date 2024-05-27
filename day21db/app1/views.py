from django.shortcuts import render
from .models import *


def studentData(request):
    allData = Student.objects.all()
    filteredData = Student.objects.filter(age=22)
    singleData = Student.objects.get(id=3)
    
    return render(request,'index.html',context={'allData':allData,'filteredData':filteredData,'singleData':singleData})


