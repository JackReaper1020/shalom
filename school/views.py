from django.shortcuts import render
from .models import Admin

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
    return render(request, 'admission.html')
# admin PAGE
def adminpage(request): 
    admins = Admin.objects.all
    return render(request, 'admin.html', {'all':admins})
