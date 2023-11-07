from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        CUSTOMER = "CUSTOMER", 'Customer'
        EMPLOYEE = "EMPLOYEE", 'Employee'
        HOSPITAL="HOSPITAL", 'hospital'

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, unique=True)  # Unique phone number field
    role = models.CharField(max_length=50, choices=Role.choices)

#class EmployeeRegistration(models.Model):
    #user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE )
    #first_name = models.CharField(max_length=30)
    #last_name = models.CharField(max_length=30) 
    #phone = models.CharField(max_length=10)
    #address = models.TextField()
    #resume_upload = models.FileField(upload_to='resumes/')
    #def __str__(self):
    #     return str(self.user)









