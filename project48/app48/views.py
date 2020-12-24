from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView
from app48.models import ProductModel
# Create your views here.
class AddProduct(CreateView):
    template_name = 'add_product.html'
    model = ProductModel
    fields = '__all__'
    success_url = '/index'

class ShowProduct(ListView):
    template_name = 'show_products.html'
    model = ProductModel

class ViewPro(ListView):
    template_name = 'view_pro.html'
    model = ProductModel
    queryset = ProductModel.objects.values('pid','name')

class UpdateProduct(UpdateView):
    template_name = 'update.html'
    model = ProductModel
    fields = ('name','price','image')
    success_url = '/show_products/'
