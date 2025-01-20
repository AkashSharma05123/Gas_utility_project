from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),  # For submitting requests
    path('track/', views.track_request, name='track_request'),      # For tracking requests
]
