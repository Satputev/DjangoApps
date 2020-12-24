from django.shortcuts import render

def showIndex(request):
    return render(request,'index.html')
account_holders=[]
def register(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    contact=request.POST.get('contact')
    job=request.POST.get('job')
    upwd=request.POST.get('pass')
    cupwd=request.POST.get('cpass')
    global account_holders
    names=[]
    passwords=[]
    if upwd==cupwd:
        for x in range(len(passwords)):
            for y in passwords[x]:
                if (name == y[0] and upwd == y[1]):
                    return render(request, 'rfail.html')
                else:
                    continue
            else:
                continue


            names.append(name)
            passwords.append(upwd)
            account_holders.append(zip(names, passwords))
        return render(request, 'rsuccess.html')





    else:
        return render(request,'rfail.html')

def login(request):
    name=request.POST.get('name')
    password=request.POST.get('password')
    for x in range(len(account_holders)):
        for y in account_holders[x]:
            if(name==y[0] and password==y[1]):
                return render(request,'lsuccess.html')
            else:
                continue

    else:
        return render(request, 'lfail.html')
