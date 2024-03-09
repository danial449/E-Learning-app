from django import forms 
from .models import *
        
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student_Profile
        fields = "__all__"

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = "__all__"