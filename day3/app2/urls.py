from django.urls import path
from .views import *

urlpatterns = [
    path("home/",app2Home),
    path("profile/",app2Profile),
]