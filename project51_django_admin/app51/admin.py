from django.contrib import admin
from django.contrib.auth.models import User, Group

from app51.models import ProductModel,EmployeeModel
# Register your models here.

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','amt','qty')
@admin.register(EmployeeModel)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','name','amt','exp')
    list_per_page = 2
    list_filter = ('amt','name')

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    readonly_fields = ['id','name']\

    # date_hierarchy = 'doj'

admin.site.unregister(User)
admin.site.unregister(Group)