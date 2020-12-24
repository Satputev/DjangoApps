"""project34_one_to_many URL Configuration

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
from app34 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showIndex,name='index'),
    path('state/',views.state,name='state'),
    path('add_state/',views.add_state,name='add_state'),
    path('show_state/',views.show_state,name='show_state'),
    path('add_district/',views.add_district,name='add_district'),
    path('save_district/',views.save_district,name='save_district'),
    path('view_dis',views.view_dis,name='view_dis'),
    path('add_taluka/',views.add_taluka,name='add_taluka'),
    path('save_t/',views.save_t,name='save_t'),
    path('view_tal/',views.view_tal,name='view_tal'),
    path('del_state/',views.del_state,name='del_state'),
    path('del_tal/',views.del_tal,name='del_tal'),
    path('del_ds/',views.del_ds,name='del_ds'),
    path('update_sate/',views.update_sate,name='update_sate'),
    path('up_sate/',views.up_sate,name='up_sate'),
    path('update_dist/',views.update_dist,name='update_dist'),
    path('up_dist/',views.up_dist,name='up_dist'),
    path('update_tal/',views.update_tal,name='update_tal'),
    path('up_tal/',views.up_tal,name='up_tal'),
]
