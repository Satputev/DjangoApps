from django.shortcuts import render,redirect
from app36.models import EmployeeModel
from django.core.paginator import Paginator
# Create your views here.
def showIndex(request):
    data=EmployeeModel.objects.all()
    ref=Paginator(data,3)
    ino=request.GET.get('ino')
    if ino:
        page=ref.page(ino)
    else:
        page=ref.page(1)

    return render(request,'index.html',{'data':page,'total':len(data)})

def add_emp(request):
    eid=request.POST.get('e1')
    ename=request.POST.get('e2')
    esal=request.POST.get('e3')
    add=request.POST.get('e4')
    img=request.FILES['e5']
    print(img)
    EmployeeModel(idno=eid,name=ename,salart=esal,address=add,photo=img).save()
    return redirect('main')

def update_emp(request):
    en=request.GET.get('no')
    return render(request,'index.html',{'data1':EmployeeModel.objects.get(idno=en),'data':EmployeeModel.objects.all()})

def Delete_emp(request):
    id=request.GET.get('no')
    EmployeeModel.objects.filter(idno=id).delete()
    return redirect('main')

def update_e(request):
    id=request.POST.get('e1')
    name=request.POST.get('e2')
    sal=request.POST.get('e3')
    addr=request.POST.get('e4')
    EmployeeModel.objects.filter(idno=id).update(name=name,salart=sal,address=addr)
    em=EmployeeModel.objects.get(idno=id)
    em.photo=request.FILES['e5']
    em.save()



    return redirect('main')