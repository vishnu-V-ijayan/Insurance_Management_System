from django.shortcuts import render
from django.http import HttpResponse
from home import *;

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Hello World..!")
    
def Sign_up(request):
    return render(request,'signup.html')

