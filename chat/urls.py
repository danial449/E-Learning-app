from django.urls import path
from .views import *

app_name = 'chat'

urlpatterns = [
    path("chat/", chat_box_view, name="chat_box_view"),
    path("get_message/", get_message_view, name="get_message_view"),
    
]
