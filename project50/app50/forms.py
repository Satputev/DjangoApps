from django import  forms
from app50.models import ProductModel
class ProductForm(forms.ModelForm):
    class Meta:
        model=ProductModel
        fields='__all__'