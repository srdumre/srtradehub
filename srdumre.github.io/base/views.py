from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings


def home(request):
    return render(request, 'base/home.html')

def inquiry_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send email (you need to configure email settings in settings.py)
        send_mail(
            subject=f'Inquiry from {name}',
            message=message,
            from_email=email,
            recipient_list=['srdumre205813@gmail.com'],  # replace with your email
        )
        
        messages.success(request, 'Inquiry sent successfully!')
        return redirect('home')  # replace 'home' with your actual home URL name
    
    return render(request, 'base/home.html')  # ensure the correct template name is used



