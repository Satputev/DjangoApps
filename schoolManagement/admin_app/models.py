from django.db import models

# Create your models here.

class AdminModel(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)


class SubjectModel(models.Model):
    sub_id=models.AutoField(primary_key=True)
    sub_name=models.CharField(max_length=64)

class ClassdModel(models.Model):
    c_id=models.AutoField(primary_key=True)
    c_name=models.CharField(unique=True,max_length=30)
    c_subjects=models.ManyToManyField(SubjectModel)



class StudentModel(models.Model):
    s_idno = models.AutoField(primary_key=True)
    s_password=models.CharField(max_length=30)
    s_name = models.CharField(max_length=30)
    s_gender = models.CharField(max_length=10)
    s_contact = models.IntegerField(unique=True)
    s_add = models.TextField()
    s_img=models.ImageField(upload_to='student_images/')
    s_class=models.ForeignKey(ClassdModel,on_delete=models.CASCADE)





class TeacherModel(models.Model):
    t_idno = models.AutoField(primary_key=True)
    t_name = models.CharField(max_length=30)
    t_gender = models.CharField(max_length=10)
    t_contact = models.IntegerField(unique=True)
    t_password=models.CharField(max_length=30)
    t_add = models.TextField()
    t_doj = models.DateField()
    t_img = models.ImageField(upload_to='teacher_images')


