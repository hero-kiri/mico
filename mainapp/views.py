from django.shortcuts import render
from .models import Doctor


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def doctor(request):
    doctors = Doctor.objects.filter(is_active=True)
    context = {
        'list_doctors': doctors
    }
    return render(request, 'doctor.html', context=context)

def testimonials(request):
    return render(request, 'testimonials.html')

def treatment(request):
    return render(request, 'treatment.html')