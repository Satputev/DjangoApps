from django.db import models

# Create your models here.
class ProductModel(models.Model):
    pid=models.IntegerField(unique=True)
    pname=models.CharField(max_length=30,unique=True)
    pprice=models.FloatField()
    pimg=models.ImageField(upload_to='products_images')