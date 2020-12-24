from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def  showHero(request):
    name=request.GET.get("a")
    if name == '1':
        return render(request, "hero.html")
    elif name =='2':
        return render(request, "heroine.html")
    else:
        return render(request, "faculty.html")






