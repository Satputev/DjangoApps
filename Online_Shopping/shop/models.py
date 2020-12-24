from django.db import models

# Create your models here.
class Register(models.Model):
    username=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=30)
    address=models.TextField()
    gender=models.CharField(max_length=10)
    dob=models.DateField()
    contact=models.IntegerField(unique=True)
