from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path("home/", home_view, name="home_view"),
    path("student/register/", student_register_view, name="student_register_view"),
    path("teacher/register/", teacher_register_view, name="teacher_register_view"),
    path("login/", user_login_view, name="user_login_view"),
    path("logout/", user_logout_view, name="user_logout_view"),
    path("verify_email/<str:token>/", verify_email_view, name="verify_email"),
]
