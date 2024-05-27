from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=40,null=True)
    price = models.FloatField(null=True)
    author = models.CharField(max_length=30,null=True)
    img = models.ImageField(null=True,upload_to='static/')

    def __str__(self) -> str:
        return self.name


