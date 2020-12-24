from django.shortcuts import render,redirect
from app32.models import NetworkModel,UserModel
from django.contrib import messages

# Create your views here.
def showIndex(request):
    return render(request,'index.html')

def registered_network(request):
    return render(request,'registered_network.html')

def network_register(request):
    nid=request.POST.get('n1')
    nname=request.POST.get('n2')
    NetworkModel(network_id=nid,network_name=nname).save()
    messages.success(request,'Network added successfully..')
    return redirect('registered_network')

def show_network(request):
    return render(request,'show_network.html',{'data':NetworkModel.objects.all()})

def add_user(request):
    return render(request,'add_user.html',{'data':NetworkModel.objects.all()})
def user_register(request):
    uid=request.POST.get('u1')
    uname=request.POST.get('u2')
    addr=request.POST.get('u3')
    cno=request.POST.get('u4')
    ntk=request.POST.getlist('u5')
    um=UserModel(user_id=uid,user_name=uname,user_address=addr,user_contact=cno)
    um.save()
    um.user_network.set(ntk)
    messages.success(request,'User added')
    return redirect('add_user')

def show_user(request):
    return render(request,'show_user.html',{'data':UserModel.objects.all()})