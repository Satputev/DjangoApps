from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
# Create your views here.
from .models import Product

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/product_list.html'


def productListView(request):
    queryset=Product.objects.all()
    context={
        'object_list':queryset
    }

    return render(request,'products/product_list.html',context)


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'


def productDetailtView(request,pk=None,*args,**kwargs):
    #instance= Product.objects.get(pk=pk)#id
    instance=get_object_or_404(Product,pk=pk)
    context = {
        'object': instance
    }

    return render(request, 'products/detail.html', context)