from django.shortcuts import render
from app1.models import Accountmodel
from django.db import IntegrityError
from  django.shortcuts import redirect
from django.db.models import F
from django.contrib import messages
from django.db.models import Q
# Create your views here.
def showIndex(request):
    return render(request,'index.html')
def insert(request):
    if request.method=='POST':
        ano=request.POST.get('accno')
        fn=request.POST.get('fn')
        ln=request.POST.get('ln')
        act=request.POST.get('acctype')
        bl=request.POST.get('balance')
        print(ano)

        try:
            Accountmodel(accno=ano,f_name=fn,l_name=ln,acc_type=act,balance=bl).save()
            return redirect('all')
        except IntegrityError:
            messages.error(request,'Account no already exist..')
            return redirect('insert')
    else:
        return render(request,'insert.html')

def all(request):
    qs=Accountmodel.objects.all()
    print(qs)
    return render(request,'all.html',{'data':qs})

def update(request):
    acc_no=request.GET.get('ano')
    qs=Accountmodel.objects.filter(accno=acc_no)
    return render(request,'update.html',{'data':qs,'acc_no':acc_no})

def updateData(request):
    fn=request.POST.get('fn')
    ln=request.POST.get('ln')
    at=request.POST.get('atype')
    bl=request.POST.get('bl')
    an=request.POST.get('accno')
    Accountmodel.objects.filter(accno=an).update(f_name=fn,l_name=ln,acc_type=at,balance=bl)
    return redirect('all')

def delete(request):
    accno=request.GET.get('ano')
    Accountmodel.objects.filter(accno=accno).delete()
    return redirect('all')

def demo(request):
    #qs=Accountmodel.objects.filter(balance__gt=10000)
   # qs=Accountmodel.objects.filter(balance__gte=10000.00)
    #qs=Accountmodel.objects.filter(f_name__startswith='R')& Accountmodel.objects.filter(l_name__startswith='K')
    # qs=Accountmodel.objects.filter(Q(f_name__startswith='K') & Q(l_name__startswith='R'))
    # print(qs)
    #
    #qs=Accountmodel.objects.exclude(accno__lt=1003)
    # qs=Accountmodel.objects.exclude(accno__range=(1004,1005))
    # print(qs)
    # print(type(qs))
    #select some fields in query
    # qs=Accountmodel.objects.filter(f_name__startswith='R').values('f_name','l_name','balance')
    # qs=Accountmodel.objects.filter(Q(f_name__startswith='K') & Q(l_name__startswith='R')).values('f_name','l_name','balance')
    # print(qs)
    # print(type(qs))
    # qs=Accountmodel.objects.filter(f_name__startswith='M').only('f_name')
    # print(qs)
    #firstname is equal to last name
    # qs=Accountmodel.objects.filter(f_name=F('l_name'))
    # print(type(qs))

    #find the 2nd highest record

    # qs=Accountmodel.objects.order_by('-balance')[1]
    # print(qs)
    # print(type(qs))

    #first name start with 'M' and accno not less then 1004
    qs=Accountmodel.objects.filter(Q(f_name__startswith='M') & ~Q(accno__lte=1003))

    return render(request,'demo.html',{'data':qs})
