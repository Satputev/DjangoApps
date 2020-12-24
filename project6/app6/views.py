from django.shortcuts import render

def eDetails(request):
    employee_info={
        "idno":101,
        "name":"Ravi",
        "salary":18500.00,
        "contact":987654321,
        "email":"ravi@gmail.com",
        "username":"ravi123",
        "password":"ravi@123",
        "age":23,
        "gender":"Female"
    }
    return render(request,"index.html",employee_info)
