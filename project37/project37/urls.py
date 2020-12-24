"""project37 URL Configuration

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
from project37 import settings
from django.conf.urls.static import static
from app37 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showIndex,name='main'),
    path('add_product/',views.add_product,name='add_product'),
    path('upate_p/',views.update_p,name= 'update_p'),
    path('delete_p/',views.delete_p,name='delete_p'),
    path('update/',views.update,name='update'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
