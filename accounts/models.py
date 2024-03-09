from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_teacher = models.BooleanField('is_teacher' , default=False)
    is_student = models.BooleanField('is_student' , default=False)
    image = models.ImageField(upload_to='user_profile_pics/', blank=True , null=True)
    email = models.EmailField(max_length=30, blank=False, null=False, unique=True)
    is_email_verified = models.BooleanField(default=False)
    email_verification_token = models.CharField(max_length=200 ,blank=True, null=True)

    def __str__(self):
        return self.username