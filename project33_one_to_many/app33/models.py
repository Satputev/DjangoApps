from django.db import models

# Create your models here.
class BiryaniType(models.Model):
    no=models.IntegerField(primary_key=True)
    type=models.CharField(max_length=30)

class Biryani(models.Model):
    no=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    price=models.FloatField()
    biryani_type=models.ForeignKey(BiryaniType,on_delete=models.CASCADE)