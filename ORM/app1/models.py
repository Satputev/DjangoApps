from django.db import models

class Accountmodel(models.Model):
    accno= models.IntegerField(unique=True)
    f_name=models.CharField(max_length=30)
    l_name=models.CharField(max_length=30)
    acc_type=models.CharField(max_length=10)
    balance=models.DecimalField(max_digits=10,decimal_places=2)
