from django.db import models

# Create your models here.
class ProductModel(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30,unique=True)
    price=models.FloatField()
    image=models.ImageField(upload_to='product_images')