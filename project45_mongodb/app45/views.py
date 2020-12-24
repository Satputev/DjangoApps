from django.shortcuts import render,redirect
from app45.forms import StudentModelForm,AdminModelForm,TeachersModelForm
from app45.models import AdminModel,TeachersModel,StudentModel
from django.db.utils import IntegrityError
from django.contrib import messages
# Create your views here.
def showIndex(request):
    return render(request,'index.html')

def add_admin(request):

    return render(request,'add_admin.html',{'form':AdminModelForm})

def save_admin(request):
    aid=request.POST.get('_id')
    aname=request.POST.get('name')
    try:
        AdminModel(_id=aid, name=aname).save()
        messages.success(request,'Admin Saved')
        return redirect('add_admin')
    except IntegrityError:
        messages.error(request,'Id already exist try different')
        return redirect('add_admin')

def show_admin(request):
    return render(request,'show_admin.html',{'data':AdminModel.objects.all()})