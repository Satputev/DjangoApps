from django.db import models

class Employee(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    contact=models.IntegerField()
    addr=models.TextField()

class Accounts(models.Model):
    bank_name = models.CharField(max_length=20)
    acc_no = models.IntegerField(primary_key=True)
    branch_no = models.IntegerField()
    ifsc_code = models.CharField(max_length=20)
    branch_address = models.TextField()
    emp=models.OneToOneField(Employee,on_delete=models.CASCADE)
