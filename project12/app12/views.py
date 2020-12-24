from django.shortcuts import render

def calc(request):
    return render(request,"index.html")
def calculate(request):
    no1=int(request.POST['fname'])
    no2=int(request.POST['sname'])
    if request.POST:
        if 'sum' in request.POST:
            total=no1+no2
        elif 'sub' in request.POST:
            total=no1-no2
        elif 'mul' in request.POST:
            total=no1*no2
        else:
            total=no1/no2

    return render(request,"index.html",{"data":total})


