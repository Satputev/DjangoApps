from django.db import models


class Employee(models.Model):
    name=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    gender=models.CharField(max_length=11)