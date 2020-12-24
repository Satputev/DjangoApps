from django.db import models

# Create your models here.
class LoginModel(models.Model):
    username=models.CharField(unique=True,max_length=30)
    password=models.CharField(max_length=30)
    user=models.CharField(max_length=20)

class WaiterModel(models.Model):
    waiter_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    contact=models.IntegerField(unique=True)
    address=models.TextField()


class MenuModel(models.Model):
    item_id=models.AutoField(primary_key=True)
    item_name=models.CharField(max_length=30,unique=True)
    item_price=models.FloatField()
    item_image=models.ImageField(upload_to='item_images/')
    def __str__(self):
        return self.item_name

class OrderTable(models.Model):
    oid=models.IntegerField(primary_key=True,unique=True)
    tbl_no=models.IntegerField()
    eat_item=models.ManyToManyField(MenuModel)
    qty=models.IntegerField()
