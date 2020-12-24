from django.db import models

# Create your models here.
class CourseModel(models.Model):
    courseId=models.IntegerField(primary_key=True)
    courseName=models.CharField(max_length=50)

class StudentModel(models.Model):
    studentId=models.IntegerField(primary_key=True)
    StudentName=models.CharField(max_length=30)
    contactNo=models.IntegerField()
    subject=models.ManyToManyField(CourseModel)