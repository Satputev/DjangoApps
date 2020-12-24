from django.shortcuts import render,redirect
from app41.forms import OwnersForm,CompaniesForm,BranchModelForm,CustomersModelForm
from app41.models import CompaniesModel,BranchesModel,OwnersModel,CustomersModel
from django.db.utils import IntegrityError
from django.contrib import messages
# Create your views here.
def showIndex(request):

    return  render(request,'index.html')
def addOwner(request):
    of=OwnersForm()
    return render(request,'addOwner.html',{'form':of})

def saveOwner(request):
    n=request.POST.get('name')
    cno=request.POST.get('contactno')
    addr=request.POST.get('address')
    gen=request.POST.get('gender')
    ph=request.FILES['photo']
    of=OwnersForm(request.POST,request.FILES)
    if of.is_valid():
        try:
            OwnersModel(name=n, contactno=cno, address=addr, gender=gen, photo=ph).save()
            messages.success(request,'saved')
            return redirect('addOwner')
        except IntegrityError:
            messages.error(request,'Contact no is already available')
            return  redirect('addOwner')
    else:
        return render(request, 'addOwner.html', {'form': of})


def showOwner(request):
    qs=OwnersModel.objects.all()
    return render(request,'showOwner.html',{'data':qs})

def addcomany(request):
    cf=CompaniesForm()
    return render(request,'addcomany.html',{'form':cf})

def save_company(request):
    cf=CompaniesForm(request.POST)
    if cf.is_valid():
        cf.save()
        messages.success(request,'company saved')
        return  redirect('addcomany')
    else:
        return render(request,'addcomany.html',{'form':cf})
def showcompany(request):
    return render(request,'showcompany.html',{'data':CompaniesModel.objects.all()})

def addBranch(request):
    return render(request,'addBranch.html',{'form':BranchModelForm()})

def save_branch(request):
    bf=BranchModelForm(request.POST)

    if bf.is_valid():
        bf.save()
        messages.success(request,'Branch saved')
        return redirect('addBranch')
    else:
        return render(request,'addBranch.html',{'form':bf})

def showBranch(request):
    return render(request,'showBranch.html',{'data':BranchesModel.objects.all()})

def add_cust(request):
    cf=CustomersModelForm()
    return render(request,'add_cust.html',{'form':cf})

def save_cust(request):
    cf=CustomersModelForm(request.POST,request.FILES)
    if cf.is_valid():
         cf.save()
         messages.success(request,'Customer saved')
         return redirect('save_cust')
    else:
        return render(request,'add_cust.html',{"form":cf})

def show_cust(request):
    return render(request,'show_cust.html',{'data':CustomersModel.objects.all()})