from django import forms 
from .models import *
from ckeditor.widgets import CKEditorWidget
        
class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = Teacher_Profile
        fields = "__all__"
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['student' , 'course' ,'feedback_text' , 'created_date']

class CourseAddForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'teacher', 'categories', 'course_image' , 'course_pdf' , 'description']