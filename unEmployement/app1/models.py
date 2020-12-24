from django.db import models

# Create your models here.

class PlayerRegister(models.Model):
    Name =models.CharField(max_length=30)
    Age =models.IntegerField()
    Contact = models.IntegerField()
    Address = models.CharField(max_length=200)
    Gender = models.CharField(max_length=10)
    Sport = models.CharField(max_length=15)
    Ptype = models.CharField(max_length=10)
    Uname = models.CharField(unique=True,max_length=30)

class LoginDetails(models.Model):
    Type=models.CharField(max_length=15)
    Uname = models.CharField(unique=True,max_length=30)
    Upwd = models.CharField(max_length=20)

class CoachingCenterRegistration(models.Model):
    name = models.CharField(max_length=30)
    addr = models.CharField(max_length=150)
    coaching_provided = models.CharField(max_length=20)
    cno = models.IntegerField()
    iId = models.CharField(unique=True,max_length=30)
    established = models.DateField()