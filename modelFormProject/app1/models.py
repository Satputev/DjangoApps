from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    username=models.IntegerField(primary_key=True,unique=True)
    password=models.CharField(max_length=20)
    name=models.CharField(max_length=30)
    salary=models.FloatField()
    gender=models.CharField(max_length=10)
    interest=models.CharField(max_length=64)
    designation=models.CharField(max_length=20)
    address=models.TextField()


