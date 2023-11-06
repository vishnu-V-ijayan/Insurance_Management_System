from django.shortcuts import render
from .models import Hospital

# Create your views here.

def getHospitals(request):
    all_hospitals = Hospital.objects.all()
    return render(request,'hospitals.html',{'all_hospitals_key':all_hospitals})