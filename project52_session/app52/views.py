from django.shortcuts import render,redirect
from app52.forms import StudentForm
from app52.models import StudentModel
# Create your views here.
def showLogin(request):
    return render(request,'login.html',{'sf':StudentForm()})

def login_student(request):
    un=request.POST.get('username')
    ps=request.POST.get('password')

    try:
        StudentModel.objects.get(username=un, password=ps)
        request.session['status']=True
        return render(request,'welcome.html')
    except StudentModel.DoesNotExist:
        return render(request, 'login.html', {'sf': StudentForm(),'error':'Invalid'})

def home(request):
    try:
        del request.session['status']
        return render(request, 'welcome.html', {'sf': StudentForm(),'error':'Invalid'})

    except KeyError:
        pass

    return redirect('')


