from django import forms

class EmployeeForm(forms.Form):
    eno=forms.IntegerField(min_value=1000 ,max_value=1999,label='Employee_no:')
    name=forms.CharField(label='Name:')
    contact=forms.IntegerField(label='Contact Number:')
    salary=forms.FloatField(label='Salary:',min_value=10000)
    desg=forms.CharField(label='Designation:')
    mail=forms.EmailField(label='Email:')
    image=forms.ImageField()
