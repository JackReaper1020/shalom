from django.db import models

class Admin(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    passwd = models.CharField(max_length=100)

    def __str__(self): 
        return self.fname + " " + self.lname
