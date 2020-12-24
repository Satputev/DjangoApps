from django.shortcuts import render,redirect
from app46.forms import ProductForm,EmployeeForm
from django.contrib import messages
# Create your views here.
def showIndex(request):
    return render(request,'index.html',{'pf':ProductForm,'ef':EmployeeForm})

def add_product(request):

    pf=ProductForm()
    if pf.is_valid():
        pf.save()
        messages.success(request,'Saved..')
        return redirect('add_product')
    else:
        return render(request,'index.html',{'pf':pf})


def add_emp(request):
    ef=EmployeeForm()

    if ef.is_valid():
        ef.save()
        messages.success(request,'Saved')
        return redirect('main')
    else:
        return render(request,'index.html',{'ef':ef})
