from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def showIndex(request):
    return render(request,'index.html')

def display(request):
    if request.method == 'POST':
        password=request.POST.get('p1')
        print(password)
        return HttpResponse("Post request data recived")
    else:
        return HttpResponse("Get request data recived")

