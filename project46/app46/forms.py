from django import forms
from django.forms import ValidationError
def validate(val):
    if val>10000:
        return val
    else:
        raise ValidationError('Invalid Amt')

class ProductForm(forms.Form):
    pid=forms.IntegerField()
    pname=forms.CharField()
    pprice=forms.FloatField(validators=[validate])

    def clean_pprice(self):
        validate(self.cleaned_data['pprice'])


class EmployeeForm(forms.Form):
    eid=forms.IntegerField(min_value=1001)
    ename=forms.CharField(min_length=3,max_length=30)
    esal=forms.FloatField(validators=[validate])