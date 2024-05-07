from django.urls import path
from .views import *

urlpatterns = [
    path('home/',app1Home),
    path('profile/',app1Profile)
]