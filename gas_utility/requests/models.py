from django.db import models

# Create your models here.
from django.db import models


class ServiceRequest(models.Model):
    REQUEST_TYPES = [
        ('Repair', 'Repair'),
        ('Installation', 'Installation'),
        ('Maintenance', 'Maintenance'),
    ]

    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES)
    details = models.TextField()
    files = models.FileField(upload_to='uploads/', null=True, blank=True)
    status = models.CharField(max_length=20, default='Pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.request_type} request from {self.customer_name}'
