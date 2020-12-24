from django.db import models

# Create your models here.

class StudentModel(models.Model):
    sname=models.CharField(max_length=30)
    contact=models.IntegerField(unique=True)
    age=models.IntegerField()
    address=models.TextField()