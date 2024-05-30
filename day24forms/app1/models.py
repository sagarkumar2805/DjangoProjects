from django.db import models

class EmployeeModel(models.Model):
    eName = models.CharField(max_length=25)
    eAge = models.IntegerField()
    email = models.EmailField()
# Create your models here.
