from django.shortcuts import render

def fdRequest(request):
    return render(request,"index.html")

def showDetails(request):

    name=request.POST["uname"]
    passwd=request.POST["upwd"]
    gmail=request.POST["email"]
    gend=request.POST["gender"]
    country=request.POST["country"]
    skills=request.POST["skills"]
    u_data={"name":name,"password":passwd,"gmail":gmail,"gender":gend,"country":country,"skills":skills}
    return render(request,"display.html",{"data":u_data})
def next(request):

    return render(request,"next.html")

