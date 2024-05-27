from django.db import models

class Author(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    age = models.IntegerField()

    def __str__(self):
        return self.firstName


class Book(models.Model):
    bookName = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
