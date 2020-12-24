from django.shortcuts import render

def display(request):
    e_details={"idno":101,"name":"Ravi","salary":185000.00}
    return render(request,'home.html',e_details)