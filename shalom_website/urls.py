"""
URL configuration for shalom_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
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
    path('login/', views.login, name="login"), 
    path('calender/', views.calender, name="calender"), 
    path('Vision&Mission/', views.views, name="views"), 
    path('StudentOfTheYear/', views.soty, name="soty"), 
    path('admissionform/', views.admission, name="admission"), 
]
