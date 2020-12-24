from django.shortcuts import render


def dispalyName(request):
    return render(request,"index.html")

def display(request):
    fname=request.POST['fname']
    lname=request.POST['lname']
    count1=0
    count2=0
    for x in fname:
        if ord(x)>=65 and ord(x)<=90 or ord(x)>=97 and ord(x)<=120:
            count1+=1
    for x in lname:
        if ord(x)>=65 and ord(x)<=90 or ord(x)>=97 and ord(x)<=120:
            count2+=1
    if(count1>=2 and count2>=2):
        ffname=fname+" "+lname
        return render(request, "index.html", {"name": ffname})

    else:
        return render(request, "index.html", {"err":"Name Must contain at least two characters..."})


