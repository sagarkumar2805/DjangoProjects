from django.http import HttpResponse

def v1(request):
    data = "<h1 style='color:red'>hello</h1>"
    return HttpResponse(data)

def v2(request):
    data = "<h1 style='color:red'>hello</h1>"
    return HttpResponse(data)

def v3(request):
    data = "<h1 style='color:red'>hello</h1>"
    return HttpResponse(data)

def v4(request):
    data = "<h1 style='color:red'>hello</h1>"
    return HttpResponse(data)

def v5(request):
    data = "<h1 style='color:red'>hello</h1>"
    return HttpResponse(data)