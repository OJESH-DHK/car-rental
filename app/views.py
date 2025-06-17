from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from itertools import chain

from .models import (
    Vehicle, Index, TripRequest, CarRentalRequest, CarRentalRequest,
    AboutUs, Testimonial, Experience, ServicesSection, ServicesOffered,
    ContactDetail, ContactMessage, Blog
)



def index(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pickup_location = request.POST.get('pickup_location')
        dropoff_location = request.POST.get('dropoff_location')
        pickup_date = request.POST.get('pickup_date')
        dropoff_date = request.POST.get('dropoff_date')
        pickup_time = request.POST.get('pickup_time')

        TripRequest.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            pickup_location=pickup_location,
            dropoff_location=dropoff_location,
            pickup_date=pickup_date,
            dropoff_date=dropoff_date,
            pickup_time=pickup_time
        )

        messages.success(request, 'Your trip request has been submitted!')
        return redirect('index')

    # Get admin-added cars
    admin_vehicles = Vehicle.objects.all()
    for v in admin_vehicles:
        v.car_type = 'admin'

    # Get user-added accepted rental cars
    user_vehicles = CarRentalRequest.objects.filter(status='accepted')

    for u in user_vehicles:
        u.car_type = 'user'

    # Combine both into one list
    vehicles = list(chain(admin_vehicles, user_vehicles))

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

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from itertools import chain

from .models import Vehicle, CarRentalRequest, CarSpec, TripRequest, Index

def car(request):
    vehicles = Vehicle.objects.all()
    accepted_rentals = CarRentalRequest.objects.filter(status='accepted')
    return render(request, 'frontend/car.html', {
        'vehicles': vehicles,
        'accepted_rentals': accepted_rentals
    })

def car_single(request, car_type, id):
    if car_type == 'admin':
        vehicle = get_object_or_404(Vehicle, id=id)
        related_cars = Vehicle.objects.filter(car_brand=vehicle.car_brand).exclude(id=vehicle.id)[:3]
        return render(request, 'frontend/car-single.html', {
            'vehicle': vehicle,
            'is_admin_car': True,
            'related_cars': related_cars,
        })

    elif car_type == 'user':
        # fetch the rental request
        rental = get_object_or_404(CarRentalRequest, id=id, status='accepted')

        # try to grab its spec record, if any
        try:
            specs = rental.specs
        except CarSpec.DoesNotExist:
            specs = None

        return render(request, 'frontend/car-single.html', {
            'rental': rental,
            'is_admin_car': False,
            'specs': specs,           # pass the CarSpec object (or None)
        })

    else:
        # invalid car_type
        return redirect('index')


def main(request):
    return render(request, 'frontend/main.html')

def pricing(request):
    return render(request, 'frontend/pricing.html')

def services(request):
    services_section = ServicesSection.objects.last()
    top_services = ServicesOffered.objects.all() if services_section else []
    context = {
        'services_section': services_section,
        'top_services': top_services
    }
    return render(request, 'frontend/services.html', context)

#book a vehicle

from .models import Vehicle, Booking
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

def book_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)

    if request.method == 'POST':
        pickup = request.POST.get('pickup_date')
        return_date = request.POST.get('return_date')
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # Save booking
        Booking.objects.create(
            vehicle=vehicle,
            full_name=name,
            email=email,
            phone=phone,
            pickup_date=pickup,
            return_date=return_date
        )

        messages.success(request, f'Booking confirmed for {vehicle.car_model} from {pickup} to {return_date}.')
        return redirect('book_vehicle', vehicle_id=vehicle.id)

    return render(request, 'frontend/booking/booking.html', {'vehicle': vehicle})

#put your car on sent 
from django.shortcuts import render, redirect
from .models import CarRentalRequest, VehicleImage

def put_car_on_rent(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        car_brand = request.POST.get('car_brand')
        car_model = request.POST.get('car_model')
        description = request.POST.get('description')
        bluebook_image = request.FILES.get('bluebook_image')
        vehicle_images = request.FILES.getlist('vehicle_images')

        # Validate image count
        if len(vehicle_images) > 10:
            return render(request, 'frontend/put_on_rent/put_your_car_on_rent.html', {
                'error': 'You can upload a maximum of 10 vehicle images.'
            })

        # Save the rental request
        rental = CarRentalRequest.objects.create(
            full_name=full_name,
            phone_number=phone_number,
            car_brand=car_brand,
            car_model=car_model,
            description=description,
            bluebook_image=bluebook_image,
        )

        # Save each uploaded image
        for image in vehicle_images:
            VehicleImage.objects.create(rental_request=rental, image=image)

        # Redirect to success page
        return redirect('rent_success')  # define this URL/template separately

    # If GET request, just show the form
    return render(request, 'frontend/put_on_rent/put_your_car_on_rent.html')

def rent_success(request):
    return render(request, 'frontend/put_on_rent/success.html') 

# views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from .models import CarRentalRequest, UserRentalBooking

def book_user_vehicle(request, id):
    rental = get_object_or_404(CarRentalRequest, id=id, status='accepted')

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pickup_date = request.POST.get('pickup_date')
        return_date = request.POST.get('return_date')

        UserRentalBooking.objects.create(
            rental=rental,
            full_name=full_name,
            email=email,
            phone=phone,
            pickup_date=pickup_date,
            return_date=return_date
        )

        messages.success(request, 'Your booking has been successfully submitted!')

        # Redirect to the same page using reverse + id
        return redirect(reverse('book_user_vehicle', kwargs={'id': rental.id}))

    return render(request, 'frontend/booking/user_vehicle_booking.html', {
        'rental': rental,
        'specs': getattr(rental, 'specs', None),
        'image': rental.images.first() if rental.images.exists() else None
    })



def contact_view(request):
    contact_info = ContactDetail.objects.first()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message_text = request.POST.get('message')

        if name and email and subject and message_text:
            # Save the message
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message_text
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill in all the fields.')

    return render(request, 'frontend/contact.html', {'contact_info': contact_info})


from django.core.paginator import Paginator

def blog_list(request):
    blog_list = Blog.objects.all().order_by('-published_date')
    paginator = Paginator(blog_list, 6)  # 6 per page
    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)
    return render(request, 'frontend/blog_list.html', {'blogs': blogs})

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    # Get recent blogs (excluding the current one)
    recent_blogs = Blog.objects.exclude(id=blog.id).order_by('-published_date')[:3]

    context = {
        'blog': blog,
        'recent_blogs': recent_blogs,
    }

    return render(request, 'frontend/blog_detail.html', context)

def booking_confirmed(request):
    return render(request, 'frontend/booking/booking_done.html')