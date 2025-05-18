from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login_user, name="login"), 
    path('adminpage/admission/', views.admission_dash, name="admission_dash"),
    path('adminpage/students/', views.student_dash, name="student"),
    path('adminpage/teachers/', views.teacher_dash, name="teacher"),
    path('approve/<int:admission_id>/', views.approve_admission, name='approve_admission'),
    path(
        'administrator/logout/',
        auth_views.LogoutView.as_view(next_page='index'),  # Redirect to admin login
        name='logout'
    ),
]
