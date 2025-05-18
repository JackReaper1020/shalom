"""
URL configuration for shalom_website project.
"""
from django.contrib import admin
from django.urls import path, include
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"), 
    path('founder/', views.founder_page, name="founder"), 
    path('gallery/', views.gallery, name="gallery"), 
    path('alumni/', views.alumni, name="alumni"), 
    path('payment/', views.payment, name="payment"), 
    path('governing/', views.govern, name="govern"), 
    path('contact/', views.contact, name="contact"), 
    path('Rules&Regulations/', views.rules, name="rules"), 
    path('calender/', views.calender, name="calender"), 
    path('Vision&Mission/', views.views, name="views"), 
    path('StudentOfTheYear/', views.soty, name="soty"), 
    path('admissionform/', views.admission, name="admission"), 
    path('adminpage/', views.adminpage, name="adminpage"), 


    # URL for administrator 
    path('administrator/', include('administrator.urls')),
    path('administrator/', include('django.contrib.auth.urls')),
]
