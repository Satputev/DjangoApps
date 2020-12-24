from django.shortcuts import render,redirect
from app1.forms import EmployeeForm
from app1.models import EmployeeModel
from django.db.utils import IntegrityError
from django.contrib import messages
def showIndex(request):

    return render(request,'index.html',{'form':EmployeeForm()})

def save(request):
    un=request.POST.get('username')
    ps=request.POST.get('password')
    nm=request.POST.get('name')
    sal=request.POST.get('salary')
    gen=request.POST.get('gender')
    inter=request.POST.getlist('interest')
    desg=request.POST.get('designation')
    addr=request.POST.get('address')
    ef=EmployeeForm(request.POST)
    if ef.is_valid():
        try:
            EmployeeModel(username=un, password=ps, name=nm, salary=sal, gender=gen, interest=inter, designation=desg,
                          address=addr).save()
            messages.success(request,'Employee saved')
            return redirect('main')
        except IntegrityError:
            messages.error(request,'Username already taken')
            return redirect('main')
    else:
        return render(request,'index.html',{'form':ef})



