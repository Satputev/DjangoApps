from django import forms
from app45.models import AdminModel,StudentModel,TeachersModel
class AdminModelForm(forms.ModelForm):
    class Meta:
        model=AdminModel
        fields='__all__'

class TeachersModelForm(forms.ModelForm):
    class Meta:
        model=TeachersModel
        fields='__all__'
class StudentModelForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields='__all__'
