from django import forms
from django.forms import ValidationError
class StudentForm(forms.Form):
    PRNno = forms.IntegerField()
    name = forms.CharField()
    address = forms.CharField()
    resume = forms.FileField()


    def clean_PRNno(self):
        no=str(self.cleaned_data['PRNno'])
        if len(no) != 6:
            raise ValidationError('Prn no must be of 6 dogits')
        else:
            return True

    def clean_name(self):
        name=self.cleaned_data['name']
        if len(name)<3 or len(name)>30:
            raise ValidationError('name contain min 3 and max 30 chars')
        else:
            return True



