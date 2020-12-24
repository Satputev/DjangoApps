"""hotel_management URL Configuration

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
from  hotel import views
from hotel_management import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showIndex,name='main'),
    path('login/',views.login,name='login'),
    path('waiters/',views.waiters,name='waiters'),
    path('register/',views.register,name='register'),
    path('edit/',views.edit,name='edit'),
    path('delete/',views.delete,name='delete'),
    path('menu/',views.menu,name='menu'),
    path('register_item/',views.register_item,name='register_item'),
    path('edit_item/',views.edit_item,name='edit_item'),
    path('delete_item/',views.delete_item,name='delete_item'),
    path('take_order',views.take_order,name='take_order'),
    path('order_taken/',views.order_taken,name='order_taken'),
    path('delete_order',views.delete_order,name='delete_order'),
    path('update_order',views.update_order,name='update_order'),
    path('updated_order/',views.updated_order,name='updated_order'),
    path('waiter_logout',views.waiter_logout,name='waiter_logout'),
    path('manager_logout',views.manager_logout,name='manager_logout'),
    path('bill/',views.bill,name='bill'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)