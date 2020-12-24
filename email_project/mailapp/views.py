from django.shortcuts import render,redirect
from django.contrib import messages
import random
from django.core.mail import send_mail
from email_project.settings import EMAIL_HOST_USER
from mailapp.models import LoginModel
def showIndex(request):
    return render(request,'index.html')
def login(request):
    un=request.POST.get('l1')
    ps=request.POST.get('l2')

    try:
        obj=LoginModel.objects.get(username=un,password=ps)
        otp=random.randint(1000,9999)
        obj.otp=otp
        obj.save()
        sub='OTP'
        msg='Hello Django user This is your generated OTP'+str(otp)
        send_mail(sub,msg,EMAIL_HOST_USER,[un])
        return render(request,'index.html',{'data':un})
    except LoginModel.DoesNotExist:
        messages.error(request,'User is not Available')
        return redirect('index')

def otp_login(request):
    otp=request.POST.get('m1')
    un=request.POST.get('m2')
    try:
        res=LoginModel.objects.get(username=un, otp=otp)
        return render(request,'loginSuccess.html',{'data':un})
    except LoginModel.DoesNotExist:
        return render(request,'index.html',{'data':un,'er':'Enter valid otp'})





