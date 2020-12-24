from django.shortcuts import render

def sInfo(request):
    student_data={"idno":101,"name":"Ravi","marks":[25,56,95,46,87,45]}
    return render(request,"main.html",student_data)