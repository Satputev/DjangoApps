from django.db import models

# Create your models here.

class Person(models.Model):
    name=models.CharField(max_length=50,blank=True)
    age=models.IntegerField(null=True)
    gender=models.CharField(max_length=10,blank=True)

    def __str__(self):
        return  self.name