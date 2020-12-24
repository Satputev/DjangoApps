from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib import messages
from app50.forms import ProductForm
from  app50.models import ProductModel
# Create your views here.
class AddProduct(View):
    def get(self,request):
        pf=ProductForm()
        return render(request,'addp.html',{'pf':pf})

    def post(self,request):
        nm=request.POST.get('pname')
        pr=request.POST.get('pprice')
        print(nm,pr)
        pf=ProductForm(request.POST)
        if pf.is_valid():
            ProductModel(pname=nm,pprice=pr).save()
            messages.success(request,'Saved successfully')
            return redirect('add_product')
        else:
            return render(request,'addp.html',{'pf':pf})
    def put(self):
        pass
    def delete(self):
        pass


class ViewProduct(View):
    def get(self,request):
        return render(request,'view_Products.html',{'data':ProductModel.objects.all()})
    def put(self,request):
        pass