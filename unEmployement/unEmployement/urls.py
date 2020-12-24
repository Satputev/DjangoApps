"""unEmployement URL Configuration

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
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showIndex,name='index'),
    path('sport/',views.sportHome,name='sport'),
    path('education/',views.educationHome,name='education'),
    path('job/',views.jobHome,name='job'),
    path('startup/',views.startUpHome,name='startup'),
    path('player_register/',views.playerRegister,name='player_register'),
    path('register_coaching_center',views.registerCochingCenter,name='register_coaching_center'),
    path('r_center/',views.rCenter,name="r_center"),
    path('p_home',views.playerHome,name='p_home'),
    path('login/',views.login,name='login'),
]
