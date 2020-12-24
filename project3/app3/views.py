from django.shortcuts import render


def showHtml(request):
    return render(request,'index.html')
