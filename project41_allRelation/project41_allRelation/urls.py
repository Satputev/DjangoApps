"""project41_allRelation URL Configuration

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

from project41_allRelation import settings
from django.conf.urls.static import static
from app41 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showIndex,name='main'),
    path('addOwner/',views.addOwner,name='addOwner'),
    path('saveOwner/',views.saveOwner,name='saveOwner'),
    path('showOwner/',views.showOwner,name='showOwner'),
    path('addcomany/',views.addcomany,name='addcomany'),
    path('save_company/',views.save_company,name='save_company'),
    path('showcompany/',views.showcompany,name='showcompany'),
    path('addBranch/',views.addBranch,name='addBranch'),
    path('save_branch/',views.save_branch,name='save_branch'),
    path('showBranch/',views.showBranch,name='showBranch'),
    path('add_cust/',views.add_cust,name='add_cust'),
    path('save_cust/',views.save_cust,name='save_cust'),
    path('show_cust/',views.show_cust,name='show_cust'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)