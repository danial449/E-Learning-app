from django.db import models
from accounts.models import CustomUser
from teachers.models import Course
# from teachers.models import Course
# Create our models here.



class Student_Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE , blank=True, null=True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    username = models.CharField(max_length = 30)
    email = models.EmailField(null=True , unique=True)
    image = models.ImageField(upload_to='teacher_profile_pics/' , null=True , blank=True)

    def __str__(self):
        return self.username

class Enrollment(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.name}"
    
class StudentNotification(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='student_sent_notifications')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='student_received_notifications')
    message = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)