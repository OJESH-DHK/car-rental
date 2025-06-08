from django.shortcuts import get_object_or_404, render

from .models import Vehicle, Index

from django.shortcuts import render
from .models import Vehicle, Index, TripRequest
from .models import AboutUs, Testimonial

def index(request):
    vehicles = Vehicle.objects.all()
    index_content = Index.objects.last()  
    context = {
        'vehicles': vehicles,
        'index': index_content
    }
    return render(request, 'index.html', context)





def about(request):
    about_content = AboutUs.objects.last()  
    testimonials = Testimonial.objects.all() 

    context = {
        'about': about_content,
        'testimonials': testimonials,
    }

    return render(request, 'about.html', context)


def blog(request):
    return render(request, 'blog.html')

def blog_single(request):
    return render(request, 'blog-single.html')

def car(request):
    return render(request, 'car.html')

def car_single(request, id):
    vehicle = get_object_or_404(Vehicle, id=id)
    return render(request, 'car-single.html', {'vehicle': vehicle})

def contact(request):
    return render(request, 'contact.html')

def main(request):
    return render(request, 'main.html')

def pricing(request):
    return render(request, 'pricing.html')

def services(request):
    return render(request, 'services.html')