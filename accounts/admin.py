from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.

class CustomUser_Admin(UserAdmin):
    list_display = ('id', 'first_name' , 'last_name', 'username', 'email')
    
    fieldsets = UserAdmin.fieldsets + (  # Include 'gender' in the 'Personal Information' section
        ('Other Information', {
            'fields': ('is_student',
                       'is_teacher',),
        }),
    )
admin.site.register(CustomUser , CustomUser_Admin)