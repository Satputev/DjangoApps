"""schoolManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from schoolManagement import settings
from django.views.generic import DeleteView
from admin_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main,name='main'),
    path('admin_after_login',views.showIndex,name='admin_after_login'),
    path('login/',views.login,name='login'),
    path('teacher/',views.Teacher.as_view(),name='teacher'),
    path('add_teacher/',views.add_teacher,name='add_teacher'),
    path('save_teacher/',views.save_teacher,name='save_teacher'),
    path('view_teacher/',views.view_teacher,name='view_teacher'),
    path('update_teacher <int:pk>/',views.UpdateTeacher.as_view(),name='update_teacher'),
    path('delete_teacher <int:pk>/',views.DeleteTeacher.as_view(),name='delete_teacher'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)