from django.contrib import admin
from myapp.models import *
# Register your models here.

class AdminPortfolio(admin.ModelAdmin):
    list_display = ['id', 'nomi', 'company_name', 'date', 'rasm1']

admin.site.register(Portfolio, AdminPortfolio)

class AdminType(admin.ModelAdmin):
    list_display = ['id', 'nomi']

admin.site.register(Type, AdminType)