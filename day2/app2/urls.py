from django.urls import path
from .views import *

urlpatterns = [
    path('app2home1/', app2home1),
    path('app2home2/', app2home2),
    path('app2home3/', app2home3),
    path('app2home4/', app2home4),
    path('app2home5/', app2home5),
]