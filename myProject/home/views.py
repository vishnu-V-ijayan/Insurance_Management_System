
from home import *;
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import User
from django.contrib.auth import authenticate, login,logout
from django.views.decorators.cache import never_cache

# Create your views here.
@never_cache
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Hello World..!")
    


    


def Sign_up(request):
    if request.method=="POST":
            fname=request.POST['fname']
            lname=request.POST['lname']
            email=request.POST['email']
            phone=request.POST['phone']
            username=email
            password=request.POST['password']
            confirm_password=request.POST['confirm_password']


            
            if password!=confirm_password:
                    messages.warning(request,"password is not matching")
                    return render(request,'signup.html')
            try:
                      if User.objects.get(username=email):
                             messages.warning(request,"Email is already taken")
                             return render(request,'signup.html')
            except Exception as identifiers:
                      pass

            user=User.objects.create_user(first_name=fname,last_name=lname,email=email,phone=phone,password=password,username=username,role='CUSTOMER')
            #user.is_active=False 
            user.save()
            return redirect('/handlelogin')
              

      
            
             
            
    return render(request,'signup.html')

def handlelogin(request):
     if request.method=="POST":
            username=request.POST['email']
            password=request.POST['password']
            myuser=authenticate(request,username=username,password=password)
            

            if myuser is not None:
                   login(request,myuser)
                   request.session['username']=username
                        #request.session['username'] =myuser.username
                   if myuser.role=='CUSTOMER':
                        
                        return redirect('/customer_home/')
                   elif myuser.role=='SELLER':
                        
                        return HttpResponse("seller login")
                   elif myuser.role=='ADMIN':
                          
                          return HttpResponse("Admin login sucess")
                          
            else:
                   messages.error(request,"enter valid credentials")
                   return redirect('/handlelogin')
     response = render(request,'login.html')
     response['Cache-Control'] = 'no-store,must-revalidate'
     return response
    

def customer_home(request):
       if 'username' in request.session:
        response = render(request,'customer_page.html')
        response['Cache-Control'] = 'no-store,must-revalidate'
        return response
       else:
             return redirect('handlelogin')




def handlelogout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')