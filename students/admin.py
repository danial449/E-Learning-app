from django.contrib import admin
from .models import *
# Register your models here.




class Student_Profile_Admin(admin.ModelAdmin):
    list_display = ('id', 'user','first_name' , 'last_name' , 'email' , 'image')
admin.site.register(Student_Profile , Student_Profile_Admin)

class Enrollment_Admin(admin.ModelAdmin):
    list_display = ('id', 'student','course')
admin.site.register(Enrollment , Enrollment_Admin)

class StudentNotificationAdmin(admin.ModelAdmin):
    list_display = ['sender' , 'receiver' ,'message' , 'timestamp' , 'is_read']
admin.site.register(StudentNotification , StudentNotificationAdmin)