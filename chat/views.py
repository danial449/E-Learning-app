from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def chat_box_view(request):
    messages = ChatMessage.objects.all().order_by('-timestamp')[:10] #Fetch the lastest 30 message
    return render(request, "chat/chat.html" , {'messages':messages})

def get_message_view(request):
    message = ChatMessage.objects.all()
    data = [{'message':message.message} for message in message]
    return JsonResponse(data , safe=False)