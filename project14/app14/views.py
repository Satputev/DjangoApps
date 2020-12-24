from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def main(request):
    uname=request.POST['username']
    upwd=request.POST['password']
    email=request.POST['email']
    if (uname=='Ravi' and upwd=='123') or (uname=="Kumar" and upwd=="123"):
        return render(request,"lmain.html",{"name":uname})
    else:
        return render(request,"err.html")

def inner(request):
    print('hi')
    return render(request,"smain.html")


def innerinner(request):
    return render(request,"innerinner.html")