from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    salart=models.FloatField()
    photo=models.ImageField(upload_to='emp_images')

    address=models.TextField()