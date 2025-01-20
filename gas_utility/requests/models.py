from django.db import models

class ServiceRequest(models.Model):
    customer_name = models.CharField(max_length=255)
    service_type = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    email = models.EmailField()  # or other fields as necessary
    details = models.TextField()  # or other fields as necessary
    attachment = models.FileField(upload_to='attachments/')  # if necessary
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Service Request {self.id}"
