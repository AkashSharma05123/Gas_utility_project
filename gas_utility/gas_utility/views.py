from django.shortcuts import redirect

def home(request):
    return redirect('submit_request')  # Redirect to the submit request page
