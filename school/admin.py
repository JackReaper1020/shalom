from django.contrib import admin
from .models import Admin
from .models import Admission
from .models import Student


# DATABSE SHOWN IN DJANGO ADMIN PAGE
admin.site.register(Admin)
admin.site.register(Admission)
admin.site.register(Student)
