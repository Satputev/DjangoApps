from django import forms

class StudentForm(forms.Form):
    name=forms.CharField(label='Name',min_length=3 ,max_length=30,strip=True )
    age=forms.IntegerField(label='Age',min_value=23,max_value=60,help_text='@Age should between 23-60 included')
    contact=forms.IntegerField(label='Contact No:',help_text='@Contact must be 10 digit and start digit must be 6/7/8/9')
    address=forms.CharField(label='Address')

    def clean_contact(self):
        cn=str(self.cleaned_data['contact'])
        if len(cn)!=10:
            raise ValueError('Contct number must contain 10 digits only')
        else:
            if(cn[0]!='6' or cn[0]!='7' or cn[0]!='8' or cn[0]!='9'):
                raise ValueError('first digit must and should start with 6/7/8/9')
            else:
                return True
