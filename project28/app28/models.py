from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    gender=models.CharField(max_length=7)
    contact=models.IntegerField(unique=True)
    email=models.CharField(max_length=30,unique=True)
    uname=models.CharField(max_length=12,unique=True)
    password=models.CharField(max_length=20)

    