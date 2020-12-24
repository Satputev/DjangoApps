from django.db import models

# Create your models here.

class stateModel(models.Model):
    cno=models.IntegerField(primary_key=True)
    state_name=models.CharField(max_length=30)

class districtModel(models.Model):
    dno=models.IntegerField(primary_key=True)
    d_name=models.CharField(max_length=30)
    state=models.ForeignKey(stateModel,on_delete=models.CASCADE)
class TalukaModel(models.Model):
    tno=models.IntegerField(primary_key=True)
    tname=models.CharField(max_length=30)
    population=models.IntegerField()
    district=models.ForeignKey(districtModel,on_delete=models.CASCADE)