from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        CUSTOMER = "CUSTOMER", 'Customer'
        EMPLOYEE = "EMPLOYEE", 'Employee'

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, unique=True)  # Unique phone number field
    role = models.CharField(max_length=50, choices=Role.choices)
