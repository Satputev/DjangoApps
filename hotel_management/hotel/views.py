from django.shortcuts import render,redirect
from django.http import HttpResponse
from hotel.models import LoginModel,WaiterModel,MenuModel,OrderTable
from django.contrib import messages
from django.db.utils import IntegrityError
from hotel.forms import LoginForm
# Create your views here.
def showIndex(request):
    return render(request,'index.html')

def login(request):
    user=request.POST.get('user')
    un=request.POST.get('u1')
    ps=request.POST.get('u2')
    rm=request.POST.getlist('u3')
    print(user,un,ps)

    if request.method=='POST':
        try:
            LoginModel.objects.get(username=un, password=ps, user=user)
            response = HttpResponse("Remember")
            if rm:
                response.set_cookie('user', un)
            request.session['username'] = un
            if user == 'manager':
                return render(request, 'manager_main.html')
            elif user =='waiter':
                return render(request,'waiter_main.html',{'ot':OrderTable.objects.all(),'data':MenuModel.objects.all()})

        except LoginModel.DoesNotExist:
            messages.success(request, 'User not exist')
            return redirect('main')
    else:
        if request.session['username']:
            return render(request, 'manager_main.html')



def waiters(request):
    sn=request.session['username']

    return render(request,'waiters.html',{'wm':WaiterModel.objects.all()})

def register(request):
    nm=request.POST.get('r1')
    cn=request.POST.get('r2')
    ad=request.POST.get('r3')
    WaiterModel(name=nm,contact=cn,address=ad).save()
    return redirect('waiters')

def edit(request):
    uid=request.POST.get('u0')
    un=request.POST.get('u1')
    uc=request.POST.get('u2')
    uadd=request.POST.get('u3')

    WaiterModel.objects.filter(waiter_id=uid).update(name=un,contact=uc,address=uadd)

    return redirect('waiters')

def delete(request):
    wid=request.GET.get('no')
    WaiterModel.objects.filter(waiter_id=wid).delete()
    return redirect('waiters')

def menu(request):
    return render(request,'menu.html',{'mm':MenuModel.objects.all()})

def register_item(request):
    iid=request.POST.get('r0')
    pn=request.POST.get('r1')
    pp=request.POST.get('r2')
    pi=request.FILES['r3']
    try:
        MenuModel(item_id=iid,item_name=pn,item_price=pp,item_image=pi).save()
        return redirect('menu')
    except IntegrityError:
        messages.error(request,'Product name already Available')
        return redirect('menu')

def edit_item(request):
    iid=request.POST.get('u0')
    itmn=request.POST.get('u1')
    itmp=request.POST.get('u2')

    try:
        MenuModel.objects.filter(item_id=iid).update(item_name=itmn,item_price=itmp)
        mm=MenuModel.objects.get(item_id=iid)
        mm.item_image=request.FILES['u3']
        mm.save()
        return redirect('menu')
    except IntegrityError:
        messages.error(request,'product name already exist')
        return redirect('menu')

def delete_item(request):
    iid=request.GET.get('no')
    MenuModel.objects.filter(item_id=iid).delete()
    return redirect('menu')

def manager_logout(request):
    del request.session['username']
    messages.success(request,'Manager logout successfully')
    return redirect('main')



def take_order(request):


    return render(request,'order.html',{'data':MenuModel.objects.all(),"ot":OrderTable.objects.all()})

def delete_order(request):
    oid=request.GET.get('oid')
    OrderTable.objects.filter(oid=oid).delete()
    return render(request,'waiter_main.html',{'ot':OrderTable.objects.all(),'data':MenuModel.objects.all()})

def update_order(request):
    oid=request.GET.get('oid')

    return render(request,'update_order.html',{'order':OrderTable.objects.get(oid=oid),'fi':MenuModel.objects.all()})

def waiter_logout(request):
    del request.session['username']
    messages.success(request,'Waiter Logout successfully..')
    return redirect('main')

def order_taken(request):
    oid=request.POST.get('r1')
    tno=request.POST.get('r2')
    fa=request.POST.getlist('r3')
    qty=request.POST.get('r4')
    print(qty)
    try:
        ot = OrderTable(oid=oid, tbl_no=tno)
        ot.save()
        ot.eat_item.set(fa)
        return render(request, 'waiter_main.html', {'ot': OrderTable.objects.all(),'data':MenuModel.objects.all()})
    except IntegrityError:
        return render(request, 'waiter_main.html', {'ot': OrderTable.objects.all(),'err':'Order id already taken'})

def updated_order(request):
    ot=OrderTable(oid=request.POST.get('u0'),tbl_no=request.POST.get('u1'))
    ot.save()
    ot.eat_item.set(request.POST.getlist('u2'))
    return render(request,'waiter_main.html',{'ot':OrderTable.objects.all(),'data':MenuModel.objects.all()})


def bill(request):
    return render(request,'bill.html',{'ot':OrderTable.objects.all()})