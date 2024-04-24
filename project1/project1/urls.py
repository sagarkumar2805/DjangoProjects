"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import *
from app2.views import *
from app3.views import *
from app4.views import *
from app5.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path("aap1home1/",aap1home1),
    path("aap1home2",app1home2),
    path("aap1home3/",app1home3),
        path("aap2home1/",aap2home1),
    path("aap2home2",app2home2),
    path("aap2home3/",app2home3),
        path("aap3home1/",aap3home1),
    path("aap3home2",app3home2),
    path("aap3home3/",app3home3),
        path("aap4home1/",aap4home1),
    path("aap4home2",app4home2),
    path("aap4home3/",app4home3),
        path("aap5home1/",aap5home1),
    path("aap5home2",app5home2),
    path("aap5home3/",app5home3),
] 
