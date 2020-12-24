from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def main(request):
    eno=int(request.POST.get('eno'))
    if(eno>=1001):
        bsal = float(request.POST.get('bsal'))
        da = bsal * 0.2
        hra = bsal * 0.4
        totalSal = bsal + da + hra
        return render(request, 'main.html', {"DA": da, "HRA": hra, "TOTALSAL": totalSal})
    else:
        return render(request,'err.html')

