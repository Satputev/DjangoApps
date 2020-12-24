from django import forms
from app41.models import OwnersModel,CompaniesModel,BranchesModel,CustomersModel
from django.forms import ValidationError

class OwnersForm(forms.ModelForm):
    gen=(('Male','MALE'),('Female','FEMALE'),('Other','OTHER'))
    gender=forms.CharField(widget=forms.RadioSelect(choices=gen))

    class Meta:
        model=OwnersModel
        fields='__all__'


    def clean_contactno(self):
        cno=str(self.cleaned_data['contactno'])
        if (len(cno)==10) and (cno[0]=='6' or cno[0]=='7' or cno[0]=='8' or cno[0]=='9'):
            return cno
        else:
            raise ValidationError('**contact no must contain ten gigits and first no must start with 6/7/8/9')






class CompaniesForm(forms.ModelForm):
    class Meta:
        model=CompaniesModel
        fields='__all__'

    def clean_c_contact(self):
        cno = str(self.cleaned_data['c_contact'])
        if (len(cno) == 10) and (cno[0] == '6' or cno[0] == '7' or cno[0] == '8' or cno[0] == '9'):
            return cno
        else:
            raise ValidationError('**contact no must contain ten gigits and first no must start with 6/7/8/9')



class BranchModelForm(forms.ModelForm):
    class Meta:
        model=BranchesModel
        fields='__all__'

    def clean_b_code(self):
        bc=str(self.cleaned_data['b_code'])
        if len(bc) != 4:
            raise ValidationError('Branch code must be four digit')
        else:
            return bc

    def clean_b_contact(self):
        cno = str(self.cleaned_data['b_contact'])
        if (len(cno) == 10) and (cno[0] == '6' or cno[0] == '7' or cno[0] == '8' or cno[0] == '9'):
            return cno
        else:
            raise ValidationError('**contact no must contain ten gigits and first no must start with 6/7/8/9')


class CustomersModelForm(forms.ModelForm):
    class Meta:
        model=CustomersModel
        fields='__all__'

    def clean_cust_contact(self):
        cno = str(self.cleaned_data['cust_contact'])
        if (len(cno) == 10) and (cno[0] == '6' or cno[0] == '7' or cno[0] == '8' or cno[0] == '9'):
            return cno
        else:
            raise ValidationError('**contact no must contain ten gigits and first no must start with 6/7/8/9')

    def clean_cust_name(self):
        cname=self.cleaned_data['cust_name']
        if len(cname)<3 and len(cname)>30:
            raise ValidationError('Name contain greater than 3 and less than 30')
        else:
            return cname







