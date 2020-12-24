from django.db import models

# Create your models here.
class AdminModel(models.Model):
    _id=models.IntegerField(unique=True)
    name=models.CharField(max_length=30)
class TeachersModel(models.Model):
    _id=models.IntegerField(unique=True)
    name=models.CharField(max_length=30)
class StudentModel(models.Model):
    _id=models.IntegerField(unique=True)
    name=models.CharField(max_length=30)