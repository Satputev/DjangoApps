from django.shortcuts import render,redirect
from form_app.models import StudentModel
# Create your views here.
from django.db.utils import IntegrityError
from form_app.forms import StudentForm
def showIndex(request):
    sf=StudentForm()
    return render(request,'index.html',{'form':sf})

def save(request):
    n=request.POST.get('name')
    a=request.POST.get('age')
    c=request.POST.get('contact')
    addr=request.POST.get('address')
    sf=StudentForm(request.POST)
    if sf.is_valid():
        try:
            StudentModel(sname=n, age=a, contact=c, address=addr).save()
            return redirect('main')
        except IntegrityError:

            return render(request, 'index.html', {'form': sf, 'error': 'Contact no already available'})
    else:
        return render(request,'index.html',{'form':sf,'error':'contact number must contain 10 digits only and first digit should start with 6/7/8/9'})





