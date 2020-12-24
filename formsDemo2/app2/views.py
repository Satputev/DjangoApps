from django.shortcuts import render,redirect
from app2.form import StudentForm
from django.contrib import messages
from app2.models import StudentModel
from django.db.utils import IntegrityError
# Create your views here.
def showIndex(request):
    sf=StudentForm()
    return render(request,'index.html',{'form':sf})

def save(request):
    no=request.POST.get('PRNno')
    nm=request.POST.get('name')
    addr=request.POST.get('address')
    rm=request.FILES['resume']
    sf=StudentForm(request.POST,request.FILES)
    if sf.is_valid():
        try:
            StudentModel(name=nm, PRNno=no, address=addr, resume=rm).save()
            messages.success(request, 'Saved')
            return redirect('main')
        except IntegrityError:
            return render(request,'index.html',{'form':sf,'err':'prn already exist'})


    else:
        return render(request,'index.html',{'form':sf})
def viewAll(requset):
    return render(requset,'index.html',{'data':StudentModel.objects.all(),'form':StudentForm()})


