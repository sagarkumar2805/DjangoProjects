from django.db import models

class StudentInfo(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)

    def __str__(self):
        return self.firstName


class ContactInfo(models.Model):
    city = models.CharField(max_length=40)
    phone = models.IntegerField()
    sid = models.OneToOneField(StudentInfo,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f"{self.phone}"
    
