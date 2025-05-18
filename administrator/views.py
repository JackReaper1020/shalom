from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from school.models import Admission, Admin, Student


def login_user(request):
    if request.method == "POST": 
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('adminpage')
        else:
            messages.success(request, ("There was an error Logging In, Try again.."))
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def admission_dash(request): 
    admission = Admission.objects.all
    return render(request, 'admission_page.html', {'admission': admission})

def student_dash(request): 
    student = Student.objects.all().order_by('current_class')
    return render(request, 'students.html', {'student': student})

def teacher_dash(request): 
    teacher = Admin.objects.all
    return render(request, 'teachers.html', {'teacher': teacher})

from django.shortcuts import get_object_or_404, redirect
from school.models import Admission, Student

# Send students from admission to student database
def approve_admission(request, admission_id):
    admission = get_object_or_404(Admission, id=admission_id)

    # Create a new Student record
    Student.objects.create(
        name=admission.name,
        current_class=admission.class_admission,
        dob=admission.dob,
        gender=admission.gender
        # map other fields as needed
    )

    # Optionally delete the admission
    admission.delete()

    return redirect('admission_dash')  # or wherever you want to go after


def logout(request): 
    logout(request)
    return redirect('index')


