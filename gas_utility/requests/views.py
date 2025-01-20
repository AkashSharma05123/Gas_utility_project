from django.shortcuts import render, get_object_or_404
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm


def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to the same page and pass a success message
            return redirect('submit_request')  # redirecting to show the form again

    else:
        form = ServiceRequestForm()

    # Add a success message to show after form submission
    success_message = "Request Submitted Successfully!" if request.method == 'POST' and form.is_valid() else None

    return render(request, 'submit_request.html', {'form': form, 'success_message': success_message})


# View for tracking and managing service requests
def track_request(request):
    if request.method == 'POST':
        # When a support agent updates the status of a request
        request_id = request.POST.get('request_id')
        status = request.POST.get('status')
        service_request = get_object_or_404(ServiceRequest, id=request_id)
        service_request.status = status
        service_request.save()

    # Fetch all service requests to display on the tracking page
    requests = ServiceRequest.objects.all()
    return render(request, 'track_request.html', {'requests': requests})
