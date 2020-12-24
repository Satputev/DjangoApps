from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def addEmployee(request):
    return render(request,'employee.html')

def view(request):
    return render(request,'view.html')

def update(request):
    return render(request,'update.html')

def delete(request):
    return render(request,'delete.html')