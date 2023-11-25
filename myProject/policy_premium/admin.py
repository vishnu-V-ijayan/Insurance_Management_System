# policy_premium/admin.py
from django.contrib import admin  
from .models import Policy, PremiumPlan  # Update the import statement

@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'coverage_details', 'premium_amount')
    search_fields = ('policy_number', 'holder_name')

@admin.register(PremiumPlan)  # Update the model name
class PremiumAdmin(admin.ModelAdmin):
    list_display = ('policy', 'amount', 'due_date', 'status')
    search_fields = ('policy__policy_number', 'policy__holder_name')
