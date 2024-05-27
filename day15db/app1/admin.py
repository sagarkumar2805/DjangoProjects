from django.contrib import admin

from .models import *

class AuthorAdmin(admin.ModelAdmin):
    list_display=['name','age']



class PublisherAdmin(admin.ModelAdmin):
    list_display=['name','age']

class BookAdmin(admin.ModelAdmin):
    list_display=['bookName','price','author_id','publisher_id']

admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Publisher,PublisherAdmin)
