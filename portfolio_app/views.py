from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            f'Message from {name}',
            message,
            email,
            [settings.EMAIL_HOST_USER],
        )
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')

def home(request):
    return render(request, 'home.html')

# Add the about view
def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def skills(request):
    return render(request, 'skills.html')

def contact(request):
    return render(request, 'contact.html')