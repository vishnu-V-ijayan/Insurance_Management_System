from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Policy, PremiumPlan, PolicyHolder, Member, HealthDetails, SelectedDisease, Payment
#from django.views.generic import View  # Import View from django.views.generic
from django.views import View  # Change the import to use View from django.views


class PolicyListView(View):
    template_name = 'policy_premium/policy_list.html'
    def get(self, request, *args, **kwargs):
        policies = Policy.objects.all()
        return render(request, self.template_name, {'policies': policies})

def view_policy(request):
    if request.method == 'POST':
        # Process form data and display policy details
        # Add your logic here based on the selections made in the view_policy.html form
        messages.success(request, 'Policy details displayed successfully.')  # Example success message
        return redirect('policy_list')  # Redirect to policy list after processing
    else:
        return render(request, 'policy_premium/view_policy.html')

def health_details(request):
    if request.method == 'POST':
        # Process health details form data
        # Add your logic here based on the selections made in the health_details.html form
        messages.success(request, 'Health details saved successfully.')  # Example success message
        return redirect('payment')  # Redirect to payment page after processing
    else:
        return render(request, 'policy_premium/health_details.html')
    
def personal_details(request):
    # Your personal_details logic here
    return render(request, 'policy_premium/personal_details.html')
# def personal_details(request):
#     if request.method == 'POST':
#         # Process personal details form data
#         # Add your logic here based on the selections made in the personal_details.html form
#         messages.success(request, 'Personal details saved successfully.')  # Example success message
#         return redirect('health_details')  # Redirect to health details page after processing
#     else:
#         return render(request, 'policy_premium/personal_details.html')

def payment(request):
    if request.method == 'POST':
        # Process payment form data
        # Add your logic here based on the selections made in the payment.html form
        messages.success(request, 'Payment successful!')  # Example success message
        return redirect('policy_list')  # Redirect to policy list after successful payment
    else:
        return render(request, 'policy_premium/payment.html')
