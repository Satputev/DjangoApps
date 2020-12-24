from django import forms
from app52.models import StudentModel

class StudentForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields='__all__'
        model=StudentModel
