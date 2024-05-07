from django.urls import path
from .views import *

app_name = 'app2'

urlpatterns = [
    path('home/',home,name='home'),
    path('index/',index,name='index')
]
