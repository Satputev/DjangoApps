from django.shortcuts import render
from app26.models import Employee
# Create your views here.
def showIndex(request):
    return render(request,"index.html")

def main(request):
    i=request.POST.get('t1')
    n=request.POST.get('t2')
    s=request.POST.get('t3')
    emp=Employee(eno=i,name=n,salary=s)
    emp.save()
    return render(request,'index.html',{"message":"Employee data saved successfully.."})
