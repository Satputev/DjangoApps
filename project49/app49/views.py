from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from app49.models import ProductModel
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.
class AddProduct(SuccessMessageMixin,CreateView):
    template_name = 'add_product.html'
    fields = '__all__'
    model = ProductModel
    success_url = '/add_product/'
    success_message = 'Saved successFully'


class ViewProduct(ListView):
    template_name = 'view_products.html'
    model = ProductModel


class ShowPro(ListView):
    template_name = 'show_pro.html'
    model = ProductModel
    queryset = ProductModel.objects.values('id','name')


class ViewDetail(DetailView):
    template_name = 'view_detail.html'
    model = ProductModel


class Update(SuccessMessageMixin,UpdateView):
    template_name = 'update.html'
    model = ProductModel
    fields = '__all__'
    success_url = '/show_pro/'
    success_message = 'Update successfully'


class Delete(DeleteView):
    template_name = 'delete.html'
    model = ProductModel
    success_url = '/show_pro/'