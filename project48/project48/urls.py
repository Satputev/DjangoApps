"""project48 URL Configuration

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
from django.views.generic import TemplateView,DetailView

from app48 import views
from project48 import settings
from app48.models import ProductModel
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',TemplateView.as_view(template_name='index.html'),name='main'),
    path('add_product/',views.AddProduct.as_view(),name='add_product'),
    path('show_products/',views.ShowProduct.as_view(),name='show_products'),
    path('view_pro/',views.ViewPro.as_view(),name='view_pro'),
    path('view_full<int:pk>/',DetailView.as_view(template_name='view_full.html',model=ProductModel),name='view_full'),
    path('update_p<int:pk>/',views.UpdateProduct.as_view(),name='update_p'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
