from django.db import models

# Create your models here.
class NetworkModel(models.Model):
    network_id=models.IntegerField(primary_key=True)
    network_name=models.CharField(max_length=20)
class UserModel(models.Model):
    user_id=models.IntegerField(primary_key=True)
    user_name=models.CharField(max_length=20)
    user_address=models.CharField(max_length=150)
    user_contact=models.IntegerField()
    user_network=models.ManyToManyField(NetworkModel)