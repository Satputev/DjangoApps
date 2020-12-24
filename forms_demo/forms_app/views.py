from django.shortcuts import render,redirect
from forms_app.forms import EmployeeForm
from forms_app.models import EmployeeModel
from django.contrib import messages
from django.db.utils import IntegrityError
from django.core.paginator import Paginator
# Create your views here.
def showIndex(request):
    ef=EmployeeForm()
    return render(request,'index.html',{'form':ef})

def save(request):
    id=request.POST.get('eno')
    nm=request.POST.get('name')
    cn=request.POST.get('contact')
    sl=request.POST.get('salary')
    dg=request.POST.get('desg')
    ml=request.POST.get('mail')
    img=request.FILES['image']
    try:
        EmployeeModel(eno=id, ename=nm, contact_no=cn, salary=sl, Designation=dg, email=ml,image=img).save()
        messages.success(request, 'Saved success')
        return redirect('main')
    except IntegrityError:
        messages.error(request,'***Employee number already exist')
        return redirect('main')
def view(request):
    em=EmployeeModel.objects.all()
    ref=Paginator(em,1)
    eno=request.GET.get('en')
    if eno:
        page=ref.page(eno)
    else:
        page=ref.page(1)

    return render(request,'view.html',{'data':page})

# def update(request):
#     eno=request.GET.get('eno')
#     data=EmployeeModel.objects.filter(eno=eno)
#     return render(request,'index.html',{'record':data})