from django.urls import path
from .views import home

urlpatterns = [
    path('',home),
    # path('about',about),
    # path('abc/',abc),
    # path('contactUs',contactUs),
    # path('profile/',profile),
]