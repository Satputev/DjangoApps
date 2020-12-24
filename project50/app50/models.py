from django.db import models
# Create your models here.
class ProductModel(models.Model):
    pid=models.AutoField(primary_key=True)
    pname=models.CharField(max_length=30)
    pprice=models.FloatField()
