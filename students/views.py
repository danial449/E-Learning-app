from django.shortcuts import render , redirect
from .models import *
from .forms import *
from teachers.models import Notification as TeacherNotification
from django.contrib import messages
# Create your views here.
def student_home_view(request):
    user = request.user
    notifications = TeacherNotification.objects.filter(receiver=user).order_by('-id')
    total_notifications = notifications.count()
    return render(request , "students/student_home.html" , {'notifications':notifications, 'user': user , 'total_notifications':total_notifications})

def course_view(request):
    courses = Course.objects.all().order_by('-id')
    user = request.user
    enrollments = Enrollment.objects.filter(student=user, course__in=courses)
    enrolled_courses_ids = enrollments.values_list('course_id', flat=True)
    return render(request, "students/course.html", {'courses': courses, 'enrolled_courses_ids': enrolled_courses_ids})

# Detial View of Teacher profile
def student_profile_detail_view(request):
    student_profile = Student_Profile.objects.get(user=request.user)
    
    return render(request, 'students/student_profile.html', {'student_profile': student_profile})


# Edit Detail view of Profile
def student_profile_edit_view(request):
    student_profile = Student_Profile.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES ,  instance=student_profile)
        if form.is_valid():
            student = form.save(commit=False)
            student_profile.user = request.user  # Ensure the user is set correctly
            student.save()
            student = request.user
            student.first_name = form.cleaned_data['first_name']
            student.last_name = form.cleaned_data['last_name']
            student.username = form.cleaned_data['username']
            student.email = form.cleaned_data['email']
            student.image = form.cleaned_data['image']
            student.save()
            messages.success(request, 'Profile successfully updated.')
            return redirect('students:student_profile_detail_view')
        else:
            print("Form is not valid:", form.errors)
    else:
        form = StudentProfileForm(instance=student_profile)

    return render(request, 'students/student_profile.html', {'form': form})

def enroll_course_view(request, course_id):
    course = Course.objects.get(id=course_id)
    user = request.user
    enrollment, created = Enrollment.objects.get_or_create(student=user, course=course)
    if created:
        # Enrollment successful
        messages.success(request , "Congratulations you enrolled!")
        # After saving the course, create notifications for all students
        teacher = course.teacher  
        
        notification = StudentNotification.objects.create(
        sender=request.user,
        receiver=teacher,
        message=f'Student {request.user.first_name} {request.user.last_name} enroll in a new course named "{course.name}"',
        course=course
        )
        notification.save()
        return redirect('students:my_courses_view')
    else:
        # Already enrolled
        return redirect('students:course_view')

def my_courses_view(request):
    user = request.user
    enrollments = Enrollment.objects.filter(student=user)
    context = {'enrollments': enrollments}
    return render(request, 'students/my_courses.html', context)