from django.shortcuts import render
from app27.models import Employee
def showIndex(request):
    return render(request,'index.html')

def register(request):
    name=request.POST.get('name')
    password=request.POST.get('password')
    email=request.POST.get('email')
    gender=request.POST.get('gender')
    cpassword=request.POST.get('cpassword')
    if(password==cpassword):
        emp=Employee(name=name,password=password,email=email,gender=gender)
        emp.save()
        return render(request,'index.html',{"smessage":"Registered successfully..."})
    else:
        return render(request,'index.html',{'fmessage':"Password should not match.."})

