from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def main(request):
    name=request.POST.get("name")
    n1=request.POST.get("n1")
    n2=request.POST.get('n2')
    sum=int(n1)+int(n2)
    return render(request,'calc.html',{'name':name,'sum':sum})