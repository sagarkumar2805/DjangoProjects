from django.shortcuts import render

def home(request):
    data = {
        "a":'''first
hello
sagar
kumar
last''',

"b":[10,20,30,40],
    }

    return render(request,'index.html',context=data)

# Create your views here.
