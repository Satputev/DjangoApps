from django.shortcuts import render,redirect
from app42.forms import ProductForm
from django.contrib import messages
from app42.models import ProductsModel
from django.core.paginator import Paginator
# Create your views here.
def showIndex(request):
    return render(request,'index.html',{'form':ProductForm()})

def save_product(request):
    pf=ProductForm(request.POST,request.FILES)

    if pf.is_valid():
        pf.save()
        messages.success(request,'Product Indserted..')
        return redirect('main')
    else:
        return render(request,'index.html',{'form':pf})
def show_product(request):
    pm=ProductsModel.objects.all()
    ref=Paginator(pm,1)
    pg=request.GET.get('p',1)
    page=ref.page(pg)
    return render(request,'show_product.html',{'data':page})

def update(request):
    pid=request.GET.get('pid')

    return render(request,'update.html',{'data':ProductsModel.objects.get(pid=pid)})

def update_product(request):
    id=request.POST.get('p1')
    name=request.POST.get('p2')
    price=request.POST.get('p3')
    img=request.FILES['p4']

    ProductsModel.objects.filter(pid=id).update(pname=name,pprice=price,pimg=img)

    return redirect('show_product')

def delete(request):
    id=request.GET.get('id')
    ProductsModel.objects.filter(pid=id).delete()
    return redirect('show_product')