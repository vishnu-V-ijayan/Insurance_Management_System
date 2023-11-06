
from home import *;
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import User
from django.contrib.auth import authenticate, login,logout
from django.views.decorators.cache import never_cache

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import User
from django.contrib.auth import authenticate, login,logout
from django.utils.encoding import DjangoUnicodeDecodeError
import re

from django.views.generic import View
from .utils import *

#for activating user account
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str
from django.template.loader import render_to_string

# Create your views here.

#email
from django.conf import settings
from django.core.mail import EmailMessage

#threading
import threading

#reset passwor generater
from django.contrib.auth.tokens import PasswordResetTokenGenerator



class EmailThread(threading.Thread):
       def __init__(self, email_message):
              super().__init__()
              self.email_message=email_message
       def run(self):
              self.email_message.send()



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
            user.is_active=False 
            user.save()
            current_site=get_current_site(request)  
            email_subject="Activate your account"
            message=render_to_string('activate.html',{
                   'user':user,
                   'domain':current_site.domain,
                   'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                   'token':generate_token.make_token(user)


            })

            email_message=EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[email],)
            EmailThread(email_message).start()
            messages.info(request,"Active your account by clicking the link send to your email")



           
            return redirect('/handlelogin')
           
             
           
    return render(request,'signup.html')

class ActivateAccountView(View):
    def get(self,request,uidb64,token):
        try:
            uid=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except Exception as identifier:
            user=None
        if user is not None and generate_token.check_token(user,token):
            user.is_active=True
            user.save()
            messages.info(request,"Account activated sucessfully")
            return redirect('/handlelogin')
        return render(request,"activatefail.html")



def handlelogin(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        myuser = authenticate(request, username=username, password=password)

        if myuser is not None:
            login(request, myuser)
            request.session['username'] = username

            if myuser.role == 'CUSTOMER':
                return redirect('/customer_home/')
            elif myuser.role == 'SELLER':
                return HttpResponse("seller login")
            elif myuser.role == 'ADMIN':
                return redirect('/admin_dashboard/')  # Redirect to the admin dashboard page

        else:
            messages.error(request, "Enter valid credentials")
            return redirect('/handlelogin')
    
    response = render(request, 'login.html')
    response['Cache-Control'] = 'no-store, must-revalidate'
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

def admin_dashboard(request):
      return render(request,"dashboard.html")

"""def employee_signup(request):
    if request.method == 'POST':
        # Handle User registration (username and password)
        email = request.POST['email']
        password = request.POST['password']

        # Set the username to the user's email
        username = email

        # Create a User instance
        user = User.objects.create_user(username=username, email=email, password=password)

        # Handle EmployeeRegistration
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        address = request.POST['address']
        resume_upload = request.FILES['resume_upload']

        # Create an EmployeeRegistration instance
        employee_registration = EmployeeRegistration(
            user=user,  # Link the User to the EmployeeRegistration
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            address=address,
            resume_upload=resume_upload
        )
        employee_registration.save()

        # Redirect to a success page or do other necessary actions
        return redirect('index')  # Change 'success_page' to the URL for the success page

    # Handle form errors and render the registration form
    return render(request, 'employee_signup.html')"""
