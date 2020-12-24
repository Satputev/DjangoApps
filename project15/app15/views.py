from django.shortcuts import render

def operation(request):
    return render(request,"index.html")

def main(request):
    no=str(request.POST['sno'])
    mark1=int(request.POST['s1'])
    mark2=int(request.POST['s2'])
    mark3=int(request.POST['s3'])
    marks=[mark1,mark2,mark3]
    res=[]
    if no[0]=='1' and no[1]=='0' and no[2]=='0' and no[3]=='1':
       if(mark1>=1 and mark1<=100 and mark2>=1 and mark2<=100 and mark3>=1 and mark3<=100):
           TotalMark=mark1+mark2+mark3
           Average=TotalMark/3
           for m in marks:
               if m>=35:
                   res.append("Pass")
               else:
                   res.append("Fail")
           result = {'Subject1': res[0], 'Subject2': res[1], 'Subject3:': res[2]}

           return render(request,"main.html",{'Tm':TotalMark,'Avg':Average,'res':result})
       else:
           return render(request, "er.html")


    else:
        return render(request,"err.html")




