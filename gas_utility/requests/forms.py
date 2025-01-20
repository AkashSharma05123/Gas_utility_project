from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['customer_name', 'service_type', 'status', 'email', 'details', 'attachment']


# requests/forms.py

# requests/forms.py
from django import forms

class TrackRequestForm(forms.Form):
    request_id = forms.IntegerField(label="Enter your Request ID")
