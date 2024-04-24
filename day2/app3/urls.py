from django.urls import path
from .views import *

urlpatterns = [
    path('app3home1/', app3home1),
    path('app3home2/', app3home2),
    path('app3home3/', app3home3),
    path('app3home4/', app3home4),
    path('app3home5/', app3home5),
]