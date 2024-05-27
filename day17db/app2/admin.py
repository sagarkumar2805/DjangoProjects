from django.contrib import admin
from .models import *

class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ['firstName','lastName']

class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['city','phone','sid']


admin.site.register(StudentInfo,StudentInfoAdmin)
admin.site.register(ContactInfo,ContactInfoAdmin)



