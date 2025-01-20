from django.contrib import admin
from .models import ServiceRequest

# Register the ServiceRequest model to manage it from the Django Admin Panel
admin.site.register(ServiceRequest)
