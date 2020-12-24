from django import forms
from app1.models import EmployeeModel
class EmployeeForm(forms.ModelForm):
    username=forms.IntegerField(min_value=101)
    password=forms.CharField(widget=forms.PasswordInput,min_length=8)
    gend=(('Male','MALE'),('Female','FEMALE'),('Other','OTHER'))
    gender=forms.CharField(widget=forms.RadioSelect(choices=(gend)))
    intr=(('Python','PYTHON'),('Django','DJANGO'),('Rest-api','REST-API'),('Data-science','DATA-SCIENCE'))
    interest=forms.CharField(widget=forms.CheckboxSelectMultiple(choices=(intr)))
    desg=(('Manager','MANAGER'),('Developer','DEVELOPER'),('Designer','DESIGNER'),('Tester','TESTER'))
    designation=forms.CharField(widget=forms.Select(choices=(desg)))

    class Meta:
        model=EmployeeModel
        fields="__all__"

    def clean_designation(self):
        des=self.cleaned_data['designation']
        sal=self.cleaned_data['salary']

        if des == 'Manager' and sal>550000 or des == 'Developer' and sal>300000 or des=='Designer' and sal>250000 or des=='Tester' and sal>220000:
            return sal
        else:
            raise forms.ValidationError('Enter valid Salary')