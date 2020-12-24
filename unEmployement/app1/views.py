from django.shortcuts import render,redirect
from app1.models import PlayerRegister,LoginDetails,CoachingCenterRegistration
from  django.db import IntegrityError
from django.contrib import messages

# Create your views here.
def showIndex(request):
    return render(request,'index.html')

def sportHome(request):
    return render(request,'sportIndex.html')

def educationHome(request):
    return render(request,'educationIndex.html')

def jobHome(request):
    return render(request,'jobIndex.html')

def startUpHome(request):
    return render(request,'startupIndex.html')

def playerRegister(request):
    name=request.POST.get('f1')
    age=request.POST.get('f2')
    contact=request.POST.get('f3')
    address=request.POST.get('f4')
    gender=request.POST.get('f5')
    sport=request.POST.get('f6')
    ptype=request.POST.get('f7')
    uname=request.POST.get('uname')
    upwd=request.POST.get('pass')
    pt='sportsMan'
    try:
        PlayerRegister(Name=name,Age=age,Contact=contact,Address=address,Gender=gender,Sport=sport,Ptype=ptype,Uname=uname).save()
        LoginDetails(Type=pt,Uname=uname,Upwd=upwd).save()
        messages.success(request,uname)
        return redirect('sport')
    except IntegrityError:
        messages.error(request,'Username already taken..')
        return redirect('sport')

def playerHome(request):
    pass



def registerCochingCenter(request):
    return render(request,'registerCochingCenter.html')

def rCenter(request):
    name=request.POST.get('c1')
    addr=request.POST.get('c2')
    coaching_provided=request.POST.get('c3')
    cno=request.POST.get('c4')
    iId=request.POST.get('c5')
    upwd=request.POST.get('c6')
    established=request.POST.get('edate')
    tp='center'

    try:
        CoachingCenterRegistration(name=name,addr=addr,coaching_provided=coaching_provided,cno=cno,iId=iId,established=established).save()
        LoginDetails(Uname=iId,Upwd=upwd,Type=tp).save()
        messages.success(request,'Registered Successfully')
        return redirect('register_coaching_center')
    except IntegrityError:
        messages.error(request,"Institute Id already taken")
        return redirect('register_coaching_center')

def login(request):
    if request.POST:
        name=request.POST.get('l1')
        upwd=request.POST.get('l2')
        u_type=request.POST.get('tp')
        try:
            ld=LoginDetails.objects.get(Uname=name,Upwd=upwd,Type=u_type)
            if ld.Type=='sportsMan':
                pl=PlayerRegister.objects.get(Ptype=u_type)


                return render(request,'player_login.html',{'name':name})
            else:
                return render(request,'center_login.html',{'name':name})
        except LoginDetails.DoesNotExist:
            messages.error(request,'User not available')
            return redirect('login')


    return render(request,'login.html')