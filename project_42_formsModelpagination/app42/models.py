from django.db import models

# Create your models here.
class ProductsModel(models.Model):
    pid=models.AutoField(primary_key=True)
    pname=models.CharField(max_length=30,unique=True)
    pprice=models.FloatField()
    pimg=models.ImageField(upload_to='product_imgs/')