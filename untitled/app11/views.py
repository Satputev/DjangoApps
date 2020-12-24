from django.shortcuts import render
def showFullName(request):
    return render(request,"index.html")