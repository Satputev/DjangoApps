from django.shortcuts import render,redirect
from django.contrib import messages
from admin_app.models import AdminModel,TeacherModel
from  admin_app.forms import TeacherForm
# Create your views here.
from  django.views.generic import ListView,CreateView,UpdateView,DeleteView
def showIndex(request):
    return render(request,'index.html')

def main(request):
    return render(request,'main.html')

def login(request):
    user=request.POST.get('u1')
    un=request.POST.get('u2')
    ps=request.POST.get('u3')

    try:
        if user == 'admin':
            AdminModel.objects.get(username=un, password=ps)
            return redirect('admin_after_login')
        elif user == 'teacher':
            TeacherModel.objects.get(t_contact=un, t_password=ps)
            return redirect('main')
        else:
            return None
    except AdminModel.DoesNotExist:
        messages.error(request, '**Wrong userneme or password')
        return redirect('main')














        return None


class Teacher(ListView):
    model =TeacherModel
    template_name = 'admin_teacher.html'


def add_teacher(request):

    return render(request,'add_teacher.html',{'tf':TeacherForm()})
def save_teacher(request):
    tf=TeacherForm(request.POST,request.FILES)
    if tf.is_valid():
        tf.save()
        messages.success(request,'Saved successfully..')
        return redirect('add_teacher')
    else:
        return render(request,'add_teacher.html',{'tf':tf})


def view_teacher(request):
    id=request.GET.get('t')
    return render(request,'view_teacher.html',{'data':TeacherModel.objects.get(t_idno=id)})


class UpdateTeacher(UpdateView):
    model = TeacherModel
    template_name = 'update_teacher.html'
    fields = '__all__'
    success_url = '/teacher/'


class DeleteTeacher(DeleteView):
    model = TeacherModel
    template_name = 'delete_teacher.html'
    success_url = '/teacher/'