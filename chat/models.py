from django.db import models
from accounts.models import CustomUser
# Create your models here.

class ChatMessage(models.Model):
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} wrote {self.message} at {self.timestamp}"