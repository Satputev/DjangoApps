from django.shortcuts import render
from app28.models import Employee
from django.db import IntegrityError

# Create your views here.
def showIndex(request):
    return render(request,'index.html')

def register(request):
    name=request.POST.get('name')
    age=request.POST.get('age')
    gender=request.POST.get('gender')
    contact=request.POST.get('contact')
    email=request.POST.get('email')
    uname=request.POST.get('uname')
    password=request.POST.get('password')
    try:
        emp = Employee(name=name, age=age, gender=gender, contact=contact, email=email, uname=uname, password=password)

        emp.save()
        return render(request,'index.html',{'message':'registered sussfully....'})
    except IntegrityError as er:
        return render(request,'index.html',{'message':"Employee already exist..."})


