from django import forms
from .models import Admission, Admin


class AdmissionForm(forms.ModelForm):
    class Meta: 
        model = Admission
        fields = ['class_admission', 'name', 'dob', 'gender', 'place_of_birth', 'nationality', 'p_number', 'aadhaar', 'bpl', 'father_name', 'father_number', 'father_occupation', 'mother_name', 'mother_number', 'mother_occupation', 'sibling_name1', 'sibling_class1', 'sibling_relation1', 'address', 'distance', 'city', 'district', 'state', 'pincode', 'religion', 'category']


class adminForm(forms.ModelForm): 
    class Meta: 
        model = Admin
        fields = ['fname', 'lname']
