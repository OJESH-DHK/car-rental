from django.shortcuts import get_object_or_404, render

from .models import Vehicle

def index(request):
    vehicles = Vehicle.objects.all() 
    return render(request, 'index.html', {'vehicles': vehicles})

def about(request):
    return render(request, 'about.html')

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