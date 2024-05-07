from django.urls import path
from .views import *

app_name = 'app1'

urlpatterns = [
    path('home/',home,name='home'),
    path('login/',login,name='login'),
    path('register',register,name='register')
]
