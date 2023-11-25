from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        CUSTOMER = "CUSTOMER", 'Customer'
        EMPLOYEE = "EMPLOYEE", 'Employee'
        HOSPITAL="HOSPITAL", 'hospital'
    
    #login_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    #phone = models.CharField(max_length=10, unique=True)  # Unique phone number field
    role = models.CharField(max_length=50, choices=Role.choices)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10, unique=True)
    address = models.TextField()
    date_of_birth = models.DateField()
    image = models.ImageField(upload_to="customer_images/", blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



#class EmployeeRegistration(models.Model):
    #user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE )
    #first_name = models.CharField(max_length=30)
    #last_name = models.CharField(max_length=30) 
    #phone = models.CharField(max_length=10)
    #address = models.TextField()
    #resume_upload = models.FileField(upload_to='resumes/')
    #def __str__(self):
    #     return str(self.user)









