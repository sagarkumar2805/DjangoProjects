from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *

@register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','author']
# Register your models here.
