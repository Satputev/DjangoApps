from django.shortcuts import render,redirect
from django.contrib import messages
from app33.models import BiryaniType,Biryani
# Create your views here.
def showIndex(request):
    return render(request,'index.html')
def add_bt(request):
    return render(request,'add_bt.html')

def save_bt(request):
    n=request.POST.get('bt1')
    t=request.POST.get('bt2')
    BiryaniType(no=n,type=t).save()
    messages.success(request,'biryani type saved..')
    return redirect('index')

def show_bt(request):
    return render(request,'show_bt.html',{'data':BiryaniType.objects.all()})

def add_b(request):
    return render(request,'add_b.html',{'data':BiryaniType.objects.all()})
def save_b(request):
    no=request.POST.get('b1')
    name=request.POST.get('b2')
    price=request.POST.get('b3')
    type=request.POST.get('b4')
    Biryani(no=no,name=name,price=price,biryani_type_id=type).save()
    messages.success(request,'biryani saved..')
    return redirect('index')
def show_b(request):
    return render(request,'show_b.html',{'data':Biryani.objects.all()})