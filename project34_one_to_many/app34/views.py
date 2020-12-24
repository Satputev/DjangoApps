from django.shortcuts import render,redirect
from django.contrib import messages
from app34.models import stateModel,districtModel,TalukaModel
# Create your views here.

def showIndex(request):
    return  render(request,'index.html')

def state(request):
    return render(request,'state.html')

def add_state(request):
    no=request.POST.get('s1')
    na=request.POST.get('s2')
    stateModel(cno=no,state_name=na).save()
    messages.success(request,'State added')
    return redirect('state')

def show_state(request):
    return render(request,'show_state.html',{'data':stateModel.objects.all()})

def add_district(request):
    return render(request,'add_district.html',{'data':stateModel.objects.all()})
def save_district(request):
    dno=request.POST.get('d1')
    dname=request.POST.get('d2')
    st=request.POST.get('d3')
    districtModel(dno=dno,d_name=dname,state_id=st).save()
    messages.success(request,'district saved')
    return redirect('add_district')
def view_dis(request):
    return render(request,'view_dis.html',{'data':districtModel.objects.all()})

def add_taluka(request):
    return render(request,'add_taluka.html',{'data':districtModel.objects.all()})

def save_t(request):
    tno=request.POST.get('t1')
    tname=request.POST.get('t2')
    p=request.POST.get('t3')
    dst=request.POST.get('t4')
    TalukaModel(tno=tno,tname=tname,population=p,district_id=dst).save()
    messages.success(request,'taluka Added')
    return redirect('add_taluka')
def view_tal(request):
    return render(request,'view_tal.html',{'data':TalukaModel.objects.all()})

def del_state(request):
    n=request.GET.get('no')
    stateModel.objects.filter(cno=n).delete()
    return redirect('show_state')

def del_tal(request):
    tno=request.GET.get('no')
    TalukaModel.objects.filter(tno=tno).delete()
    return redirect('view_tal')

def del_ds(request):
    no=request.GET.get('no')
    districtModel.objects.filter(dno=no).delete()
    return redirect('view_dis')

def update_sate(request):
    sn=request.GET.get('no')
    return render(request,'update_sate.html',{'data':stateModel.objects.get(cno=sn)})

def up_sate(request):
    sn=request.POST.get('s1')
    name=request.POST.get('s2')
    stateModel.objects.filter(cno=sn).update(state_name=name)
    return redirect('show_state')

def update_dist(request):
    dn=request.GET.get('no')
    return render(request,'update_dist.html',{'data':districtModel.objects.get(dno=dn),'data1':stateModel.objects.all()})
def up_dist(request):
    dno=request.POST.get('d1')
    dname=request.POST.get('d2')
    st=request.POST.get('d3')
    districtModel.objects.filter(dno=dno).update(d_name=dname,state_id=st)
    return redirect('view_dis')
def update_tal(request):
    tn=request.GET.get('no')
    return render(request,'update_tal.html',{'data':TalukaModel.objects.get(tno=tn),'data1':districtModel.objects.all()})


def up_tal(request):
    no=request.POST.get('t1')
    name=request.POST.get('t2')
    popl=request.POST.get('t3')
    dst=request.POST.get('t4')
    TalukaModel.objects.filter(tno=no).update(tname=name,population=popl,district_id=dst)
    return redirect('view_tal')

















