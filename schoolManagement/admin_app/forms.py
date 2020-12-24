from django import forms
from admin_app.models import TeacherModel,SubjectModel,ClassdModel,StudentModel
from django.forms import ValidationError
class TeacherForm(forms.ModelForm):
    t_name=forms.CharField(label='Teacher Name')
    t_password=forms.CharField(widget=forms.PasswordInput)
    gend=[('male','Male'),('female','Female'),('other','Other')]
    t_gender=forms.CharField(widget=forms.RadioSelect(choices=gend))
    t_contact = forms.IntegerField(label='Contact')
    t_add = forms.CharField(label='Address')
    t_doj = forms.DateInput()
    t_img = forms.ImageField(label='Profile Photo')


    class Meta:
        model=TeacherModel
        fields='__all__'


    def clean_t_contact(self):
        cnt=str(self.cleaned_data['t_contact'])

        if len(cnt) !=10 or (cnt[0] !='9' and cnt[0] !='8' and cnt[0] != '7' and cnt[0] != '6'):
            raise ValidationError('Contact must be 10 characters & it should be start with 9/8/7/6')
        else:
            return cnt



