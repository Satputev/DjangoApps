from django.db import models

# Create your models here.
class LoginModel(models.Model):
    username=models.EmailField(unique=True,max_length=30)
    password=models.CharField(max_length=20)
    otp=models.IntegerField(null=True)