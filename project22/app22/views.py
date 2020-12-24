from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def main(request):
    m=request.GET.get("m")
    name=request.POST.get("name")
    interest=request.POST.getlist('interest')


    if m=='1':
        url="https://www.youtube.com/embed/K0eDlFX9GMc"
    elif m=='2':
        url="https://www.youtube.com/embed/x_7YlGv9u1g"
    else:
        url="https://www.youtube.com/embed/6L6XqWoS8tw"
    return render(request,'main.html',{"url":url,"name":name,"interest":interest})

