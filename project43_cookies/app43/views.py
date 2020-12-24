from django.shortcuts import render,redirect
from app43.models import ProductModel

# Create your views here.
def showIndex(request):
    ck=len(request.COOKIES)

    return render(request,'index.html',{'data':ProductModel.objects.all(),'ck':ck-1})

def addproduct(request):
    pid= request.GET.get('pid')
    pname=request.GET.get('pname')
    response=redirect('main')
    #response.set_cookie(pid,value=pname)
    response.set_cookie(pid,value=pname,max_age=20)

    return response
def show_cart(request):
    ckd={}
    cookie_data=request.COOKIES
    for x,y in cookie_data.items():
        if x =='csrftoken':
            continue
        else:
            ckd[x]=y


    return render(request,'show_cart.html',{'ck_data':ckd})

def delete_ck(request):
    cid=request.GET.get('cid')
    res=redirect('show_cart')
    res.delete_cookie(cid)
    return res