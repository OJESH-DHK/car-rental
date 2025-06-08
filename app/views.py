from django.shortcuts import get_object_or_404, render
from .models import (
    Vehicle, Index, TripRequest, AboutUs, Testimonial, Experience, 
    ServicesSection, ServicesOffered
)

def index(request):
    vehicles = Vehicle.objects.all()
    index_content = Index.objects.last()  
    context = {
        'vehicles': vehicles,
        'index': index_content
    }
    return render(request, 'frontend/index.html', context)

def about(request):
    about_content = AboutUs.objects.last()  
    testimonials = Testimonial.objects.all() 
    experience = Experience.objects.last()
    context = {
        'experience': experience,
        'about': about_content,
        'testimonials': testimonials,
    }
    return render(request, 'frontend/about.html', context)

def blog(request):
    return render(request, 'frontend/blog.html')

def blog_single(request):
    return render(request, 'frontend/blog-single.html')

def car(request):
    return render(request, 'frontend/car.html')

def car_single(request, id):
    vehicle = get_object_or_404(Vehicle, id=id)
    return render(request, 'frontend/car-single.html', {'vehicle': vehicle})

def contact(request):
    return render(request, 'frontend/contact.html')

def main(request):
    return render(request, 'frontend/main.html')

def pricing(request):
    return render(request, 'frontend/pricing.html')

def services(request):
    services_section = ServicesSection.objects.last()
    top_services = ServicesOffered.objects.all()[:4] if services_section else []
    context = {
        'services_section': services_section,
        'top_services': top_services
    }
    return render(request, 'frontend/services.html', context)
