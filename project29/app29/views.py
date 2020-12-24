from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'login.html')
def welcome(request):
    name=request.POST.get('uname')
    password=str(request.POST.get('password'))
    userType=request.POST.get('user')


    if (userType=='Student'):
        msg='Welcome Student'
        nme=name



    elif (userType == 'Faculty'):
        msg = 'Welcome Faculty'
        nme = name


    else:
        msg='Welcome Admin'
        nme=name
    return render(request,'welcome.html',{"data":[{"message":msg},{"name":nme}]})



