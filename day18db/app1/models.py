from django.db import models

class Student(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    age = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.firstName
    

class Teacher(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    age = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.firstName
    


