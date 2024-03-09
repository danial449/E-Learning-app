from django.contrib import admin
from .models import *
# Register your models here.




class Teacher_Profile_Admin(admin.ModelAdmin):
    list_display = ('id', 'user','first_name' , 'last_name' , 'email' , 'image')
admin.site.register(Teacher_Profile , Teacher_Profile_Admin)

class CousreCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_courses')

    def display_courses(self, obj):
        # Get the course related to this category
        courses = Course.objects.filter(categories=obj)
        # Return a comma-separated list of course names
        return ", ".join([course.name for course in courses])

    # Set a more descriptive column header
    display_courses.short_description = 'Courses in Category'

admin.site.register(Course_Category , CousreCategoryAdmin)

class CousreAdmin(admin.ModelAdmin):
    list_display = ( 'id' , 'name' , 'categories')

admin.site.register(Course , CousreAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['student' , 'course' ,'feedback_text' , 'created_date']
admin.site.register(Feedback , FeedbackAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['sender' , 'receiver' ,'message' , 'timestamp' , 'is_read']
admin.site.register(Notification , NotificationAdmin)