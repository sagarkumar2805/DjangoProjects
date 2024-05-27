from django.contrib import admin
from .models import *
from django.contrib.admin.decorators import register


@register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["firstName","lastName","age","address"]
