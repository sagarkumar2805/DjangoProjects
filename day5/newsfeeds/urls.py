from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', news),
    path('movies/', movies),
    path('sports/', sports),
    path('politics/', politics),

]