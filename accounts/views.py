from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import login  , authenticate, logout
from django.urls import reverse
from django.contrib import messages
from .models import CustomUser
import uuid
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from .forms import LoginForm , UserignUpForm
from teachers.models import *
from students.models import *
# Create your views here.
def home_view(request):
    return render(request , "accounts/home.html")

def student_register_view(request):
    if request.method == 'POST':
        form = UserignUpForm(request.POST , request.FILES)
        if form.is_valid():
            user = form.save(commit=False) 
            user.is_student = True  
            user.is_staff = False  
            user.is_email_verified = False
            user.email_verification_token = str(uuid.uuid4())
            user.save() 
            
            # making profile during registration
            profile = Student_Profile.objects.create(
                user=user,
                first_name=user.first_name,
                last_name=user.last_name,
                username=user.username,
                email=user.email,
                image=user.image
            )

            current_site = get_current_site(request)
            subject = 'Activate Your Account'
            activation_link = f'http://{current_site}/account/verify_email/{user.email_verification_token}/'
            message = f'click the link to activate your account:{activation_link}'
            email_from = settings.EMAIL_HOST_USER
            recipeient_list = [user.email]
            send_mail(subject, message, email_from, recipeient_list)

            return redirect('accounts:user_login_view')
        else:
            print("Form is not valid:", form.errors)
    else:
        form = UserignUpForm()
    return render(request , "accounts/register.html", {'form':form})

def teacher_register_view(request):
    msg = None
    if request.method == 'POST':
        form = UserignUpForm(request.POST , request.FILES)
        if form.is_valid():
            user = form.save(commit=False)  
            user.is_teacher = True  
            user.is_staff = False  
            user.is_email_verified = False
            user.email_verification_token = str(uuid.uuid4())
            user.save()

            # making profile during registration
            profile = Teacher_Profile.objects.create(
                user=user,
                first_name=user.first_name,
                last_name=user.last_name,
                username=user.username,
                email=user.email,
                image=user.image
            )

            current_site = get_current_site(request)
            subject = 'Activate Your Account'
            activation_link = f'http://{current_site}/account/verify_email/{user.email_verification_token}/'
            message = f'click the link to activate your account:{activation_link}'
            email_from = settings.EMAIL_HOST_USER
            recipeient_list = [user.email]
            send_mail(subject, message, email_from, recipeient_list)

            return redirect('accounts:user_login_view')
        else:
            print("Form is not valid:", form.errors)
    else:
        form = UserignUpForm()
    return render(request , "accounts/teacher_register.html", {'form':form  })

def verify_email_view(request , token):
    try:
        user = CustomUser.objects.get(email_verification_token = token)
        if user:
           user.is_email_verified = True
           user.email_verification_token = None
           user.save()
           return redirect('accounts:user_login_view')
    except:
        return HttpResponse("Activation Link is Invalid")
    
def user_login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # Authenticate user
            user = authenticate(username=username, password=password)
            
            if user is not None and user.is_student and user.is_email_verified:
                login(request, user)
                return redirect('students:student_home_view')
            elif user is not None and user.is_teacher and user.is_email_verified:
                login(request, user)
                return redirect('teachers:teacher_home_view')
            else:
               messages.error(request, 'Invalid Credentials')
    else:
        form = LoginForm()
    return render(request , 'accounts/login.html', {'form':form})

def user_logout_view(request):
    logout(request)
    return redirect('accounts:home_view')