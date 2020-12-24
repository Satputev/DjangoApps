from django.shortcuts import render
from app30.models import Person
from django.db.models import Q
# Create your views here.
def showIndex(request):
    return render(request,'index.html')

def getall(request):
    qs=Person.objects.all()
    return render(request,'getall.html',{'data':qs})

def getall1(request):
    qs=Person.objects.only('name','age')#it return all fields objects
    return render(request,'getall1.html',{'data':qs})

def fetchDistinct(request):
    qs=Person.objects.values('name','age').distinct()
    return render(request,'getall1.html',{'data':qs})

def fetchSpecific(request):
    qs=Person.objects.all()[:4]
    return render(request,'getall.html',{'data':qs})
def fetchFromToSpecific(request):
    qs=Person.objects.all()[1:4]
    return render(request,'getall.html',{'data':qs})

def filter1(request):
    qs=Person.objects.filter(age__gt=24)
    return render(request,'getall.html',{'data':qs})
def filter2(request):
    qs=Person.objects.filter(age__gte=24)
    return render(request,'getall.html',{'data':qs})
def filter3(request):
    qs=Person.objects.filter(age__lt=24)
    return render(request,'getall.html',{'data':qs})

def filter4(request):
    qs=Person.objects.exclude(age=23)
    return render(request,'getall.html',{'data':qs})
def filter5(request):
    qs=Person.objects.filter(age__range=(23,30))
    return render(request,'getall.html',{'data':qs})#both are enclusive
def like1(request):
    #qs1=Person.objects.filter(name__icontains='a')
    #qs2=Person.objects.filter(name__icontains='a')
    #qs3=Person.objects.filter(name__istartswith='k')
    # q4=Person.objects.filter(name__startswith='n')
    # qs5=Person.objects.filter(name__iendswith='A')
    qs6=Person.objects.filter(name__endswith='a')
    return render(request,'getall.html',{'data':qs6}) #difference between contains and icontains

def inDemo(request):
    qs=Person.objects.filter(age__in=range(20,31))#the difference between in operator and range is :in in it ckecks in given iterables ans
    return render(request,'getall.html',{'data':qs})
def logical_operators1(request):
    qs=Person.objects.filter(gender='male',age__gt=25)
    return render(request,'getall.html',{'data':qs})
def logical_operators2(request):
    qs=Person.objects.filter(Q(gender='male')| Q(age__gt=25))
    return render(request,'getall.html',{'data':qs})

def logical_operators3(request):
    qs=Person.objects.values('name').filter(age__gt=25).exclude(gender='male')
    return render(request,'getall.html',{'data':qs})
def nullDemo(request):
    # qs1=Person.objects.values('name','gender').filter(age__isnull=True)
    # #or
    # qs2=Person.objects.filter(age=None)
    # qs=Person.objects.filter(age__isnull=False)
    # qs=Person.objects.exclude(age__isnull=True)
    qs=Person.objects.values('name','gender').exclude(age=None)
    return render(request,'getall.html',{'data':qs})
def order1(request):
    qs=Person.objects.order_by('age')
    return render(request,'getall.html',{'data':qs})
def order2(request):
    qs=Person.objects.order_by('-age')
    return render(request,'getall.html',{'data':qs})
def insertDemo(request):
    qs=Person.objects.create(name='Ravi kumar',gender='male',age=26)
    print(type(qs))
    return render(request,'getall.html',)