from django.shortcuts import render

def show(request):
    return render(request,"index.html")

def main(request):
    n1=int(request.POST.get('n1'))
    final=[]
    nos=[]
    for x in range(1,n1+1):
        l1=[]
        for y in range(1,11):
            g=str(x)+"x"+str(y)+" = "+str(x*y)
            l1.append(g)
        final.append(l1)





    return render(request,"home.html",{"data":final})
