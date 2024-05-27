from django.shortcuts import render
from .forms import *

def registerForm(request):
    form = Register()
    data = {'form':form}

    return render(request,'form.html',context=data)
# Create your views here.
