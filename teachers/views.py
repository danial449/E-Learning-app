from django.shortcuts import render , redirect
from .models import *
from .forms import *
from django.contrib import messages
from students.models import Enrollment , StudentNotification
# Create your views here.
def teacher_home_view(request):
    students = CustomUser.objects.filter(is_student=True)
    notifications = StudentNotification.objects.filter(sender__in=students).order_by('-id')
    total_notifications = notifications.count()
    return render(request , "teachers/teacher_home.html" , {'notifications':notifications, 'students': students , 'total_notifications':total_notifications})

# Detial View of Teacher profile
def teacher_profile_detail_view(request):
    teacher_profile = Teacher_Profile.objects.get(user=request.user) 

    
    return render(request, 'teachers/teacher_profile.html', {'teacher_profile': teacher_profile})


# Edit Detail view of Profile 
def teacher_profile_edit_view(request):
    teacher_profile = Teacher_Profile.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = TeacherProfileForm(request.POST, request.FILES ,  instance=teacher_profile)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher_profile.user = request.user  # Ensure the user is set correctly
            teacher.save()
            teacher = request.user
            teacher.first_name = form.cleaned_data['first_name']
            teacher.last_name = form.cleaned_data['last_name']
            teacher.username = form.cleaned_data['username']
            teacher.email = form.cleaned_data['email']
            teacher.image = form.cleaned_data['image']
            teacher.save()
            messages.success(request, 'Profile successfully updated.')
            return redirect('teachers:teacher_profile_detail_view')
        else:
            print("Form is not valid:", form.errors) 
    else:
        form = TeacherProfileForm(instance=teacher_profile)

    return render(request, 'teachers/teacher_profile.html', {'form': form})

def add_course_view(request):
    categories = Course_Category.objects.all()
    if request.method == 'POST':
        form = CourseAddForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()

            # After saving the course, create notifications for all students
            students = CustomUser.objects.filter(is_student=True)  
            for student in students:
              notification = Notification.objects.create(
              sender=request.user,
              receiver=student,
              message=f'Teacher {request.user.first_name} {request.user.last_name} added a new course named "{course.name}"',
              course=course
              )
              notification.save()

            return redirect('teachers:teacher_courses_view' ,id=request.user.id)  
        else:
            print(form.errors)
    else:
        form = CourseAddForm()
    return render(request, 'teachers/course_add.html', {'form': form , 'categories':categories})

def teacher_courses_view(request , id):
    teacher = CustomUser.objects.get(id=id)  # Replace Vendor with your actual vendor model

    # Filter services based on the current vendor
    courses = Course.objects.filter(teacher=teacher).order_by('-id')
    return render(request, 'teachers/teacher_courses.html', {'courses': courses , 'teacher':teacher})

def course_delete_view(request , course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    messages.success(request, 'Cousre deleted successfully.')
    return redirect('teachers:teacher_courses_view', id=request.user.id)

def course_detail_view(request , course_id):
    course = Course.objects.get(id=course_id)
    enrollments = Enrollment.objects.filter(course=course)
    feedback = course.feedback.all()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feeback=form.save(commit=False)
            feeback.course = course
            feeback.student = request.user
            feeback.save()
            return redirect('teachers:course_detail_view' , course_id=course.id)
        else:
            print(form.errors)
    else:
        form=FeedbackForm()
    return render(request , 'teachers/course_detail.html', {'course':course , 'feedback':feedback , 'form':form , 'enrollments':enrollments})

def cancel_enrollment_view(request, enrollment_id , course_id):
    enrollment = Enrollment.objects.get(id=enrollment_id)
    course = Course.objects.get(id=course_id)
    enrollment.delete()
    messages.success(request , f"Remove Enrollment of {enrollment.student.first_name} {enrollment.student.last_name}")
    return redirect('teachers:course_detail_view' ,course_id=course.id)

import logging
def teacher_search_view(request):
    search_query = request.GET.get('search_query', '')
    
    if search_query:
        students = CustomUser.objects.filter(is_student=True, first_name__icontains=search_query)
        teachers = CustomUser.objects.filter(is_teacher=True, first_name__icontains=search_query)
        template_name = 'teachers/user_search_results.html'
    else:
        logging.warning('No data found')
    
    return render(request, template_name, {'students': students, 'teachers': teachers, 'search_query': search_query})