from django.shortcuts import render,redirect
from app35.models import Employee,Accounts
from django.contrib import messages
# Create your views here.
def showIndex(request):
    return render(request,'index.html')
def add_acc(request):
    return render(request,'add_acc.html',{'data':Employee.objects.all()})

def add_emp(request):
    return render(request,'add_emp.html')

def save_emp(request):
    eid=request.POST.get('e1')
    en=request.POST.get('e2')
    ec=request.POST.get('e3')
    ea=request.POST.get('e4')
    Employee(idno=eid,name=en,contact=ec,addr=ea).save()
    messages.success(request,'Employee saved..')
    return redirect('add_emp')

def save_acc(request):
    bname=request.POST.get('a1')
    an=request.POST.get('a2')
    bno=request.POST.get('a3')
    ifsc=request.POST.get('a4')
    addr=request.POST.get('a5')
    emp=request.POST.get('a6')
    Accounts(bank_name=bname,acc_no=an,branch_no=bno,ifsc_code=ifsc,branch_address=addr,emp_id=emp).save()
    messages.success(request,'Account saved')
    return redirect('add_acc')

def show_acc(request):
    return render(request,'show_acc.html',{'data':Accounts.objects.all()})

def update_acc(request):
    accn=request.GET.get('no')
    qs=Accounts.objects.get(acc_no=accn)
    return render(request,'update_acc.html',{'data':qs,'data1':Employee.objects.all()})

def delete_acc(request):
    acn=request.GET.get('no')
    Accounts.objects.filter(acc_no=acn).delete()
    return redirect('show_acc')

def update_accdata(request):
    acn=request.POST.get('a1')
    eid=request.POST.get('a2')
    brn=request.POST.get('a3')
    ifsc=request.POST.get('a4')
    bn=request.POST.get('a5')
    baddr=request.POST.get('a6')
    Accounts.objects.filter(acc_no=acn).update(bank_name=bn,branch_no=brn,ifsc_code=ifsc,branch_address=baddr,emp_id=eid)
    return redirect('show_acc')
def show_emp(request):
    return render(request,'show_emp.html',{'data':Employee.objects.all()})

def update_emp(request):
    idno=request.GET.get('no')
    return render(request,'update_emp.html',{'data':Employee.objects.get(idno=idno)})

def update_empl(request):
    eid=request.POST.get('e1')
    ename=request.POST.get('e2')
    contact=request.POST.get('e3')
    addr=request.POST.get('e4')
    Employee.objects.filter(idno=eid).update(name=ename,contact=contact,addr=addr)
    return redirect('show_emp')

def delete_emp(request):
    eid=request.GET.get('no')
    Employee.objects.filter(idno=eid).delete()
    return redirect('show_emp')