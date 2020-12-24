from django.db import models

# Create your models here.

class CommonModel(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    amt=models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        abstract=True



class ProductModel(CommonModel):
    qty=models.IntegerField()
    class Meta:
        verbose_name_plural='Product'

class EmployeeModel(CommonModel):
    exp=models.FloatField()
    class Meta:
        verbose_name_plural='Employee'