from  django import forms
from django.forms import  ValidationError
from  hotel.models import LoginModel
import re
class LoginForm(forms.ModelForm):
    username=forms.CharField(min_length=3)
    password=forms.CharField(widget=forms.PasswordInput,min_length=3)
    def _clean_fields(self):
        ps=self.cleaned_data['password']
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"
        pat = re.compile(reg)
        mat = re.search(pat, ps)
        if mat:
            return ps
        else:
            raise ValidationError('password must gte 8 chrs and contain at least 1 char,1 no,1 ss')

    class Meta:
        model=LoginModel
        fields='__all__'