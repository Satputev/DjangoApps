"""project45_mongodb URL Configuration

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
from django.urls import path,include
from app45 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showIndex,name='main'),
    path('add_admin/',views.add_admin,name='add_admin'),
    path('save_admin/',views.save_admin,name='save_admin'),
    path('show_admin/',include(),name='show_admin'),
]
