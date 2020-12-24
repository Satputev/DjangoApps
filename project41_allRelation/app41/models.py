from django.db import models

# Create your models here.
class OwnersModel(models.Model):
    name=models.CharField(max_length=30)
    contactno=models.IntegerField(primary_key=True)
    address=models.TextField()
    gender=models.CharField(max_length=10)
    photo=models.ImageField(upload_to='owners_images/')

    def __str__(self):
        return self.name

class CompaniesModel(models.Model):
    c_name=models.CharField(max_length=30)
    ISONO=models.IntegerField(primary_key=True)
    mainBranch_addr=models.TextField()
    c_contact=models.IntegerField(unique=True)
    owner=models.OneToOneField(OwnersModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.c_name


class BranchesModel(models.Model):
    branch_name=models.CharField(max_length=30)
    b_code=models.IntegerField(primary_key=True)
    b_address=models.TextField()
    b_contact=models.IntegerField(unique=True)
    company=models.ForeignKey(CompaniesModel,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.b_code)

class CustomersModel(models.Model):
    cust_name=models.CharField(max_length=30)
    cust_contact=models.IntegerField(primary_key=True)
    cust_addr=models.TextField()
    cust_image=models.ImageField(upload_to='cust_images/')
    br_name=models.ManyToManyField(BranchesModel)

    def __str__(self):
        return self.cust_name

