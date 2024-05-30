from django.shortcuts import render,HttpResponse
from .forms import RegisterForm
from .models import RegisterFormModel


def registerForm(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            email = request.POST['email']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            age = request.POST['age']

            obj = RegisterFormModel(email=email,first_name=first_name,last_name=last_name,age=age)

            obj.save()        

        return HttpResponse("<h1>submitted</h1>")
    
    else:
        form = RegisterForm()
        data = {'form':form}
        return render(request,'form.html',context=data)
