from django.http import HttpResponse
from .models import *
from datetime import datetime
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import Group,User
from .models import Timetable  # Import your model
from .forms import TimetableForm

@csrf_exempt
def mylogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Check user's groups
            groups = user.groups.all()

            if groups.exists():
                group_names = [group.name for group in groups]

                # Debugging: print group names
                print(f"User {username} belongs to groups: {group_names}")

                # Redirect based on group membership
                if 'Chief' in group_names:
                    return redirect('chief_dashboard')
                elif 'Teacher' in group_names:
                    return redirect('teacher_dashboard')
                elif 'Office' in group_names:
                    return redirect('staff_dashboard')
                elif 'Admin' in group_names:
                    return redirect('/admin/')
                else:
                    messages.error(request, 'You do not belong to any group.')
            else:
                messages.error(request, 'You do not belong to any group.')
        else:
            messages.error(request, 'Invalid username or password.')
            print("Invalid login credentials")  # Debugging line

    return render(request, 'exam/login.html')


def chief_dashboard(request):
    return render(request, 'exam/chief.html')

def teacher_dashboard(request):
    return render(request, 'exam/teacher.html')

def staff_dashboard(request):
    return render(request, 'exam/office.html')

def exam(request):
    if request.method == "POST":
        # If the form is submitted
        form = TimetableForm(request.POST)  # Assuming you have a form for validation
        if form.is_valid():
            # If form data is valid, save it to the database
            form.save()
            return redirect('chief_dashboard')  # Redirect to a success page or any other URL
        else:
            # If form data is invalid, render the form again with errors
            return render(request, "exam/exam.html", {'form': form})
    else:
        # If it's a GET request, just render the form
        form = TimetableForm()  # Assuming you have a form for validation
        return render(request, "exam/exam.html", {'form': form})

def allot_duty(request):
    exams = Exam.objects.all()
    print(list(exams))
    return render(request, 'exam/allot_duty.html', {'exams': exams})



def edit_teacher(request):
    return render(request,'exam/edit_teacher.html')

