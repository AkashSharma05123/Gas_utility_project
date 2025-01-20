from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('confirmation')  # Redirect to confirmation page
    else:
        form = ServiceRequestForm()

    return render(request, 'request/submit_request.html', {'form': form})



def confirmation(request):
    return render(request, 'request/confirmation.html')


# requests/views.py

# requests/views.py



# requests/views.py
# requests/views.py
from django.shortcuts import render
from .models import ServiceRequest
from .forms import TrackRequestForm

def track_request(request):
    form = TrackRequestForm()
    request_details = None

    if request.method == 'POST':
        form = TrackRequestForm(request.POST)
        if form.is_valid():
            request_id = form.cleaned_data['request_id']
            try:
                request_details = ServiceRequest.objects.get(id=request_id)
            except ServiceRequest.DoesNotExist:
                request_details = None

    return render(request, 'request/track_request.html', {'form': form, 'request_details': request_details})

