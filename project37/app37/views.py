from django.shortcuts import render,redirect
from app37.models import Products
from django.core.paginator import Paginator
# Create your views here.
def showIndex(request):
    ref=Paginator(Products.objects.all(),1)
    pn=request.GET.get('p')
    if pn:
        page=ref.page(pn)
    else:
        page=ref.page(1)
    return render(request,'index.html',{'data':page})

def add_product(request):
    pid=request.POST.get('p1')
    pname=request.POST.get('p2')
    pt=request.FILES['p3']
    Products(pid=pid,pname=pname,photo=pt).save()
    return redirect('main')
def update_p(request):
    pid=request.GET.get('pid')
    return render(request,'index.html',{'data2':Products.objects.all(),'data1':Products.objects.get(pid=pid)})
def delete_p(request):
    pid=request.GET.get('pid')
    Products.objects.filter(pid=pid).delete()
    return redirect('main')

def update(request):
    id=request.POST.get('p1')
    name=request.POST.get('p2')
    Products.objects.filter(pid=id).update(pname=name)
    p=Products.objects.get(pid=id)
    p.photo=request.FILES['p3']
    p.save()
    return redirect('main')