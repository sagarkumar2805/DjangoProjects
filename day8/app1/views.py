from django.shortcuts import render

def info(request):
    data = {'name':'Sagar','age':'24','gender':'Male', 'img':'https://cdn.pixabay.com/photo/2018/09/08/09/48/ornament-3662184_1280.jpg'}
    return render(request,'index.html',context=data)
