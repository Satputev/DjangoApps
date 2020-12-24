from django.db import models

# Create your models here.
class Products(models.Model):
    pid=models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=30)
    photo=models.ImageField(upload_to='emp_imgs')