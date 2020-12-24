from django import forms
from  app42.models import ProductsModel
from django.forms import ValidationError
class ProductForm(forms.ModelForm):
    class Meta:
        model=ProductsModel
        fields='__all__'
        exclude=('pid',)
        labels={'pname':'Product Name','pprice':'Product Price','pimg':'Product Image'}

    def clean_pprice(self):
        price=self.cleaned_data['pprice']

        if price < 1:
            raise ValidationError('price should be greater than "0"')
        else:
            return price
