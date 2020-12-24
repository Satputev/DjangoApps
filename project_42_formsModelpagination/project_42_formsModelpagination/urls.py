"""project_42_formsModelpagination URL Configuration

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
from project_42_formsModelpagination import settings
from django.conf.urls.static import static
from app42 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showIndex,name='main'),
    path('save_product/',views.save_product,name='save_product'),
    path('show_product/',views.show_product,name='show_product'),
    path('update/',views.update,name='update'),
    path('update_product/',views.update_product,name='update_product'),
    path('delete/',views.delete,name='delete'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
