from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def main(request):
    m=request.GET.get("m")
    if m=='1':
        url="https://www.youtube.com/embed/4RaUVs45hNU"
    elif m=='2':
        url="https://www.youtube.com/embed/dFGYK-iRMgw"
    else:
        url="https://www.youtube.com/embed/RwiOq-dJgDM"
    return render(request,'movie.html',{'link':url})
