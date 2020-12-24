from django.db import models

# Create your models here.
class StudentModel(models.Model):
    PRNno=models.IntegerField(unique=True)
    name=models.CharField(max_length=30)
    address=models.TextField()
    resume=models.FileField(upload_to='resumes/')
    dateOfApplication=models.DateField(auto_now=True)
