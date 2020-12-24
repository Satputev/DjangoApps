from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    eid=models.AutoField(primary_key=True)
    ename=models.CharField(max_length=30)
    esal=models.FloatField()


class ProductModel(models.Model):
    pid=models.AutoField(primary_key =True)
    pname=models.CharField(max_length=30)
    pprice=models.FloatField()

    class Meta:
        app_label='product'