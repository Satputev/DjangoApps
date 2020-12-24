"""project_30 URL Configuration

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
from app30 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showIndex,name='index'),
    path('getall/',views.getall,name='getall'),
    path('getall1/',views.getall1,name='getall1'),
    path('fetchDistinct/',views.fetchDistinct,name='fetchDistinct'),
    path('firstFourRow/',views.fetchSpecific,name='fetchSpecific'),
    path('fetchFromToSpecific/',views.fetchFromToSpecific,name='fetchFromToSpecific'),
    path('filter1/',views.filter1,name='filter1'),
    path('filter2/',views.filter2,name='filter2'),
    path('filter3/',views.filter3,name='filter3'),
    path('filter4/',views.filter4,name='filter4'),
    path('filter5',views.filter5,name='filter5'),
    path('like1/',views.like1,name='like1'),
    path('in/',views.inDemo,name='in'),
    path('logical_operators1/',views.logical_operators1,name='logical_operators1'),
    path('logical_operators2/',views.logical_operators2,name='logical_operators2'),
    path('logical_operators3/',views.logical_operators3,name='logical_operators3'),
    path('nullDemo/',views.nullDemo,name='nullDemo'),
    path('order1/',views.order1,name='order1'),
    path('order2',views.order2,name='order2'),
    path('insertDemo/',views.insertDemo,name='insertDemo')
]
