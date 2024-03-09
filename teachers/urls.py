from django.urls import path
from .views import *

app_name = 'teachers'

urlpatterns = [
    path("home/", teacher_home_view, name="teacher_home_view"),
    path("teacher/profile/", teacher_profile_detail_view, name="teacher_profile_detail_view"),
    path("teacher/profile/edit/", teacher_profile_edit_view, name="teacher_profile_edit_view"),
    path("teacher/course/<int:id>", teacher_courses_view, name="teacher_courses_view"),
    path("teacher/course/add/", add_course_view, name="add_course_view"),
    path("teacher/course/delete/<int:course_id>", course_delete_view, name="course_delete_view"),
    path("teacher/course/detail/<int:course_id>", course_detail_view, name="course_detail_view"),
     path('cancel_enrollment/<int:enrollment_id>/<int:course_id>/', cancel_enrollment_view, name='cancel_enrollment_view'),
     path('search/', teacher_search_view, name='teacher_search_view'),
]
