from django.db import models

# Create your models here.
GENDER_CHOICES=[
    ('M','MALE'),
    ('F','FEMALE'),
    ('O','OTHERS')
]

class Patient(models.Model):
    patient_id=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    slug=models.SlugField(max_length=30)
    age=models.PositiveIntegerField()
    gender=models.CharField(choices=GENDER_CHOICES,max_length=10)
    dateofbirth=models.DateField()
    mobile_number=models.CharField(max_length=10)
    email=models.EmailField()
    address=models.TextField()
    profileimage=models.ImageField(upload_to="images/patient/")

