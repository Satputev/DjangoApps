"""project49 URL Configuration

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
from project49 import settings
from app49 import views
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',TemplateView.as_view(template_name='index.html'),name='main'),
    path('add_product/',views.AddProduct.as_view(),name='add_product'),
    path('view_products/',views.ViewProduct.as_view(),name='view_products'),
    path('show_pro/',views.ShowPro.as_view(),name='show_pro'),
    path('view_detail<int:pk>/',views.ViewDetail.as_view(),name='view_detail'),
    path('update<int:pk>/',views.Update.as_view(),name='update'),
    path('delete<int:pk>/',views.Delete.as_view(),name='delete'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)