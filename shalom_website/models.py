from django.db import models

class Administrator(modes.Model): 
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    passwd = models.CharField(max_length=100)
    num = models.IntegerField(max_length=10)
