from django.contrib import admin

from app41.models import BranchesModel,OwnersModel,CompaniesModel,CustomersModel
# Register your models here.
admin.register(OwnersModel,CompaniesModel,BranchesModel,CustomersModel)(admin.ModelAdmin)