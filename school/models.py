from django.db import models

class Admin(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    passwd = models.CharField(max_length=100)

    def __str__(self): 
        return self.fname + " " + self.lname


class Admission(models.Model):
    # STUDENT INFORMATION
    class_admission = models.CharField(max_length=2)
    name = models.CharField(max_length=100)
    dob = models.DateField(max_length=8)
    gender = models.CharField(max_length=4)
    place_of_birth = models.CharField(max_length=100)
    nationality  = models.CharField(max_length=50)
    p_number  = models.CharField(max_length=10)
    aadhaar  = models.CharField(max_length=12)
    bpl  = models.CharField(max_length=3)

    # PARENT INFORMATION
        #Father Information
    father_name   = models.CharField(max_length=50)
    father_number = models.CharField(max_length=10)
    father_occupation  = models.CharField(max_length=50)

        # MOTHER Information
    mother_name  = models.CharField(max_length=50)
    mother_number = models.CharField(max_length=10)
    mother_occupation = models.CharField(max_length=50)

    income = models.CharField(max_length=12)


    # Information of sibling studying in this school
    sibling_name1 = models.CharField(max_length=50)
    sibling_class1 = models.CharField(max_length=50)
    sibling_relation1 = models.CharField(max_length=50)

 
    # Studnet's Address Information
    address = models.CharField(max_length=50)
    distance = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)


    # Reservation Information
    religion = models.CharField(max_length=50)
    category = models.CharField(max_length=50)


    def __str__(self): 
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(max_length=8)
    gender = models.CharField(max_length=4)
    current_class = models.CharField(max_length=2)
    def __str__(self): 
        return self.name
