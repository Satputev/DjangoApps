from django.shortcuts import render
from shop.models import Register
import random
from django.core.mail import send_mail
from Online_Shopping.settings import EMAIL_HOST_USER
# Create your views here.
def showIndex(request):
    return render(request,'home.html')

def login(request):
    uname=request.POST.get('uname')
    upwd=request.POST.get('upwd')
    try:
        data=Register.objects.get(username=uname,password=upwd)
    except Register.DoesNotExist:
        return render(request,'home.html',{'err':'Username or password wrong'})


    return render(request,'login.html',{'uname':uname,'upwd':upwd})
def forgot_password(request):
    return render(request,'forgot_password.html')

def forgot_pass(request):
    mail_id=request.POST.get('email')
    otp=random.randint(1000,9999)

