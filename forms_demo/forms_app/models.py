from django.db import models

# Create your models here.


class EmployeeModel(models.Model):
    eno=models.IntegerField(unique=True)
    ename=models.CharField(max_length=30)
    contact_no=models.IntegerField()
    salary=models.FloatField()
    Designation=models.CharField(max_length=20)
    email=models.EmailField()
    image=models.ImageField(upload_to='emp_images/')
