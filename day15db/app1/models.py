from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=25,null=True)
    age = models.IntegerField(null=True)

class Publisher(models.Model):
    name = models.CharField(max_length=30,null=True)
    age = models.IntegerField(null=True)

class Book(models.Model):
    bookName = models.CharField(max_length=30,null=True)
    price = models.IntegerField(null=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE,null=True)


    