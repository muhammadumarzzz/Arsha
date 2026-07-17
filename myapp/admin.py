from django.contrib import admin
from myapp.models import *
# Register your models here.

class AdminPortfolio(admin.ModelAdmin):
    list_display = ['id', 'nomi', 'company_name', 'date', 'rasm1']

admin.site.register(Portfolio, AdminPortfolio)

class AdminType(admin.ModelAdmin):
    list_display = ['id', 'nomi']

admin.site.register(Type, AdminType)

from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_class', 'order', 'is_active', 'created_at')
    
    list_editable = ('order', 'is_active')
    
    search_fields = ('title', 'description')
    
    list_filter = ('is_active', 'created_at')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'position',
        'order',
        'is_active',
        'created_at',)

    list_filter = (
        'is_active',
        'created_at',
    )

    search_fields = (
        'full_name',
        'position',
    )

    ordering = (
        'order',
        '-created_at',
    )

    list_editable = (
        'order',
        'is_active',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )

    fieldsets = (
        ('Asosiy maʼlumotlar', {
            'fields': (
                'full_name',
                'position',
                'bio',
                'image',
            )
        }),

        ('Ijtimoiy tarmoqlar', {
            'fields': (
                'twitter_url',
                'facebook_url',
                'instagram_url',
                'linkedin_url',
            )
        }),

        ('Sozlamalar', {
            'fields': (
                'order',
                'is_active',
            )
        }),

        ('Vaqt', {
            'fields': (
                'created_at',
                'updated_at',
            )
        }),
    )

