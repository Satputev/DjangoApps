"""project35_one_to_one URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app35 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showIndex,name='main'),
    path('add_acc/',views.add_acc,name='add_acc'),
    path('add_emp/',views.add_emp,name='add_emp'),
    path('save_emp/',views.save_emp,name='save_emp'),
    path('save_acc/',views.save_acc,name='save_acc'),
    path('show_acc/',views.show_acc,name='show_acc'),
    path('update_acc/',views.update_acc,name='update_acc'),
    path('delete_acc/',views.delete_acc,name='delete_acc'),
    path('update_accdata/',views.update_accdata,name='update_accdata'),
    path('show_emp/',views.show_emp,name='show_emp'),
    path('update_emp',views.update_emp,name='update_emp'),
    path('update_empl/',views.update_empl,name='update_empl'),
    path('delete_emp/',views.delete_emp,name='delete_emp'),

]
