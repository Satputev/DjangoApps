from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,'homepage.html',{})

def product_page(request):
    return  render(request,'product_page.html',{})

def about_page(request):
    return render(request,"about_page.html",{})

def contact_page(request):
    return  render(request,'contact_page.html',{})