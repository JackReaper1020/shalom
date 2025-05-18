from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Admin,Admission,Student
from django.contrib.auth.decorators import login_required
from .forms import AdmissionForm, adminForm

def index(request): 
    return render(request, 'index.html')


# FOUNDER PAGE
def founder_page(request): 
    return render(request, 'Founder.html')
# ALIMNI PAGE
def alumni(request): 
    return render(request, 'Alumnides.html')
# GALLERY PAGE
def gallery(request): 
    return render(request, 'GALLERY CHOICE.html')
# GOVERNING PAGE
def govern(request): 
    return render(request, 'GOVERNING BODY.html')
# PAYMENT PAGE
def payment(request): 
    return render(request, 'paymentoffees.html')
# RULES&REGULATION PAGE
def rules(request): 
    return render(request, 'RULES AND REGS.html')
# CLAENDER PAGE
def calender(request): 
    return render(request, 'SCHOOL CALENDER.html')
# studofyegallery PAGE
def soty(request): 
    return render(request, 'stuofyegallery.html')
# views PAGE
def views(request): 
    return render(request, 'VISION AND MISSION.html')
# contact PAGE
def contact(request): 
    return render(request, 'CONTACT.html')
# login PAGE
def login(request): 
    return render(request, 'login.html')
# admission PAGE
def admission(request): 
    if request.method == "POST": 
        form = AdmissionForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(request, 'Thankyou.html')
        else: 
            print("Invalid form.", form.errors)
            return redirect(request, 'admission.html')
    else: 

        return render(request, 'admission.html')
# admin PAGE
def adminpage(request): 
    admins = Admin.objects.count()
    student = Student.objects.count()
    admission = Admission.objects.count()
    return render(request, 'admin.html', {'student': student, 'admin':admins, 'admission':admission})
