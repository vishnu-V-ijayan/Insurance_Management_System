from django.contrib import admin
from .models import Hospital,Hospital_Type

# Register your models here.

#admin.site.register(Hospital)
#admin.site.register(Hospital_Type)

class HospitalAdmin(admin.ModelAdmin):
    prepopulated_fields={
        'slug': ('name',)
    }

admin.site.register(Hospital,HospitalAdmin)
admin.site.register(Hospital_Type)