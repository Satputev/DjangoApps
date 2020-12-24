from django.shortcuts import render,redirect
from app31.models import CourseModel,StudentModel
from django.contrib import messages
# Create your views here.
def showIndex(request):
    return render(request,'index.html')
def add_course(request):
    return render(request,'add_course.html')
def save_course(request):
    cid=request.POST.get('c1')
    cname=request.POST.get('c2')
    CourseModel(courseId=cid,courseName=cname).save()
    messages.success(request,'Saved')
    return redirect('add_course')
def view_course(request):
    return render(request,'view_course.html',{'data':CourseModel.objects.all()})

def add_student(request):

    return render(request,'add_student.html',{'data':CourseModel.objects.all()})

def register_student(request):
    sid=request.POST.get('s1')
    sname=request.POST.get('s2')
    scno=request.POST.get('s3')
    ac=request.POST.getlist('s4')
    sm=StudentModel(studentId=sid,StudentName=sname,contactNo=scno)
    sm.save()
    sm.subject.set(ac)
    messages.success(request,'saved')
    return redirect('add_student')

def view_students(request):
    return render(request,'view_students.html',{'data':StudentModel.objects.all()})

def update_course(request):
    cn=request.GET.get('no')
    return render(request,'update_course.html',{'data':CourseModel.objects.get(courseId=cn)})


def update_c(request):
    cid=request.POST.get('c1')
    cn=request.POST.get('c2')
    CourseModel.objects.filter(courseId=cid).update(courseName=cn)
    return redirect('view_course')


def delete_course(request):
    n=request.GET.get('no')
    CourseModel.objects.filter(courseId=n).delete()
    return redirect('view_course')

def update_student(request):
    n=request.GET.get('no')
    return render(request,'update_student.html',{'data':StudentModel.objects.get(studentId=n),'data1':CourseModel.objects.all()})



def update_s(request):
    no=request.POST.get('s1')
    name=request.POST.get('s2')
    cno=request.POST.get('s3')
    sub=request.POST.getlist('s4')
    StudentModel.objects.filter(studentId=no).update(StudentName=name,contactNo=cno)
    StudentModel(studentId=no).subject.set(sub)
    return  redirect('view_students')



def delete_student(request):
    sno=request.GET.get('no')
    StudentModel.objects.filter(studentId=sno).delete()
    return redirect('view_students')