from django.contrib import admin
from django.contrib.admin.decorators import register
# Register your models here.

from .models import *


@register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','age','address']



