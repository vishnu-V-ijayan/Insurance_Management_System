# policy_premium/urls.py
from django.urls import path
from .views import PolicyListView, view_policy, health_details, personal_details, payment

urlpatterns = [
    path('policy_list/', PolicyListView.as_view(), name='policy_list'),  # Use as_view() for class-based views
    #path('policy_list/', policy_list, name='policy_list'),
    path('view_policy/', view_policy, name='view_policy'),
    path('health_details/', health_details, name='health_details'),
    path('personal_details/', personal_details, name='personal_details'),
    path('payment/', payment, name='payment'),
]
