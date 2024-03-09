from django.urls import path
from .views import *

app_name = 'students'

urlpatterns = [
    path("home/student/", student_home_view, name="student_home_view"),
    path("course/", course_view, name="course_view"),
    path("profile/", student_profile_detail_view, name="student_profile_detail_view"),
    path("profile/edit/", student_profile_edit_view, name="student_profile_edit_view"),
    path('enroll/<int:course_id>/', enroll_course_view, name='enroll_course_view'),
    path('enrolled/course/', my_courses_view, name='my_courses_view'),
]
