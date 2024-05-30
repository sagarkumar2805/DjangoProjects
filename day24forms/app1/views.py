from django.shortcuts import render,HttpResponse

from .forms import EmployeeForm
from .models import EmployeeModel

def employeeRegisterForm(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            eName = request.POST['eName']
            eAge = request.POST['eAge']
            email = request.POST['email']

            obj = EmployeeModel(eName = eName, eAge=eAge,email=email)
            obj.save()

        return HttpResponse("<h1>submitted</h1>")
    
    form = EmployeeForm()
    data = {'form':form}

    return render(request,'form.html',context=data)

        


