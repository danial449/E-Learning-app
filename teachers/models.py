from django.db import models
from accounts.models import CustomUser
from django.utils import timezone
# Create our models here.




class Teacher_Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE , blank=True, null=True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    username = models.CharField(max_length = 30)
    email = models.EmailField(null=True , unique=True)
    image = models.ImageField(upload_to='teacher_profile_pics/' , null=True , blank=True)

    def __str__(self):
        return self.username

class Course_Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    categories=models.ForeignKey(Course_Category ,on_delete=models.CASCADE , blank=True ,null=True) 
    course_image = models.ImageField(upload_to='course_cover_pics/' , null=True , blank=True)
    course_pdf = models.FileField(upload_to='course_pdfs/', null=True, blank=True)
    description = models.TextField(max_length=500,null=True, blank=True)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE , related_name='feedback')
    feedback_text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now , null=True, blank=True)


    def __str__(self):
        return str(self.student)

class Notification(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_notifications')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_notifications')
    message = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)