from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib import messages
from app.models import (
    Vehicle, Index, TripRequest, AboutUs, Testimonial, Experience, 
    ServicesSection, ServicesOffered, CarRentalRequest, ContactDetail, ContactMessage,
    Blog
)
from app.models import Vehicle, VehicleImage
from .forms import ContactDetailForm, BlogForm
from app.models import Index
from app.models import AboutUs, Vehicle
from django.contrib import messages
from app.models import CarRentalRequest, CarSpec
from .forms import TestimonialForm 
from app.models import ServiceImage

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard/base/admin_base.html')


def services(request):
    services_section = ServicesSection.objects.last()
    services_offered_list = ServicesOffered.objects.select_related('image').all()
    context = {
        'services_section': services_section,
        'services_offered_list': services_offered_list
    }
    return render(request, 'dashboard/services/ad_services.html', context)


def add_service(request):
    if request.method == 'POST':
        service_name = request.POST.get('service_name')
        service_desc = request.POST.get('service_desc')
        service_image_file = request.FILES.get('service_image')

        if service_name and service_desc:
            new_service = ServicesOffered.objects.create(
                services_offered=service_name,
                services_offered_desc=service_desc
            )

            # Save image if uploaded
            if service_image_file:
                ServiceImage.objects.create(service=new_service, image=service_image_file)

            messages.success(request, "Service added successfully!")
            return redirect('service')
        else:
            messages.error(request, "All fields are required.")
    
    return render(request, 'dashboard/services/ad_add_services.html')

from django.shortcuts import render, redirect
from django.contrib import messages

def edit_services_section(request):
    services_section = ServicesSection.objects.last()

    if request.method == 'POST':
        main_image = request.FILES.get('main_image')
        second_image = request.FILES.get('second_image')

        if not services_section:
            services_section = ServicesSection()

        if main_image:
            services_section.main_image = main_image
        if second_image:
            services_section.second_image = second_image

        services_section.save()
        messages.success(request, "Services section updated successfully.")
        return redirect('service')  

    context = {'services_section': services_section}
    return render(request, 'dashboard/services/edit_services_section.html', context)

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

def edit_service_offered(request, id):
    service_item = get_object_or_404(ServicesOffered, id=id)

    if request.method == 'POST':
        title = request.POST.get('services_offered')
        description = request.POST.get('services_offered_desc')
        service_image_file = request.FILES.get('service_image')

        # Update title and description
        service_item.services_offered = title
        service_item.services_offered_desc = description
        service_item.save()

        # Handle image update/create
        if service_image_file:
            # If related image object exists, update it; else create new
            if hasattr(service_item, 'image'):
                service_item.image.image = service_image_file
                service_item.image.save()
            else:
                ServiceImage.objects.create(service=service_item, image=service_image_file)

        messages.success(request, "Service updated successfully.")
        return redirect('service')

    context = {
        'service_item': service_item,
    }
    return render(request, 'dashboard/services/edit_service_offered.html', context)


def delete_service(request, id):
    service = get_object_or_404(ServicesOffered, id=id)
    service.delete()
    messages.success(request, "Service deleted successfully.")
    return redirect('service')



def about_view(request):
    about = AboutUs.objects.first() 
    return render(request, 'dashboard/about/ad_viewabout.html', {'about': about})


#trip request 
def trip_request(request):
    trip_requests = TripRequest.objects.all()
    return render(request,'dashboard/trip_request/triprequest.html', {'trip_requests': trip_requests})



def ad_about(request):
    about = AboutUs.objects.first()

    if request.method == "POST":
        about.title = request.POST.get("title")
        about.description = request.POST.get("description")

        if 'index_image' in request.FILES:
            about.index_image = request.FILES['index_image']
        if 'sub_image' in request.FILES:
            about.sub_image = request.FILES['sub_image']

        about.save()
        messages.success(request, "About section updated successfully.")
        return redirect('ad_viewabout')

    context = {
        'about': about
    }
    return render(request, 'dashboard/about/ad_about.html', context)

#add Vehicle

def ad_vehicle(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'dashboard/vehicle/ad_vehicle.html', {'vehicles': vehicles})





def admin_add_vehicle(request):
    if request.method == 'POST':
        try:
            # Basic validation
            if len(request.FILES.getlist('vehicle_images')) > 10:
                messages.error(request, "You can upload a maximum of 10 vehicle images.")
                return redirect('admin_add_vehicle')  # Adjust this name to your actual URL name

            # Create the Vehicle object
            vehicle = Vehicle.objects.create(
                car_brand=request.POST.get('car_brand'),
                car_model=request.POST.get('car_model'),
                price_per_day=request.POST.get('price_per_day'),
                transmission=request.POST.get('transmission'),
                seats=request.POST.get('seats'),
                mileage=request.POST.get('mileage') or 0,
                luggage_capacity=request.POST.get('luggage_capacity') or 0,
                image=request.FILES.get('image')  # Main image
            )

            # Handle multiple vehicle images
            for image in request.FILES.getlist('vehicle_images'):
                VehicleImage.objects.create(vehicle=vehicle, image=image)

            messages.success(request, "Vehicle added successfully!")
            return redirect('admin_vehicles')  # Redirect to the vehicle list page

        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('admin_add_vehicle')

    return render(request, 'dashboard/vehicle/add_vehicle.html')




from app.models import CarRentalRequest

def admin_rental_requests_view(request):
    rentals = CarRentalRequest.objects.all().order_by('-submitted_at')
    return render(request, 'dashboard/put_on_rent/car_rental_requests.html', {'rentals': rentals})

def admin_rental_detail(request, id):
    rental = get_object_or_404(CarRentalRequest, id=id)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        rental.status = new_status
        rental.save()
        return redirect('admin_rental_requests')  # or the same page: redirect('admin_rental_detail', id=id)

    context = {
        'rental': rental,
    }
    return render(request, 'dashboard/put_on_rent/rental_detail.html', context)


def admin_contact_details(request):
    contact_detail = ContactDetail.objects.first()
    return render(request, 'dashboard/admin_contact_details.html', {'detail': contact_detail})

def admin_contact_detail_edit(request):
    contact_detail, created = ContactDetail.objects.get_or_create(pk=1)

    if request.method == 'POST':
        form = ContactDetailForm(request.POST, instance=contact_detail)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact details updated successfully.")
            return redirect(reverse('admin_contact_details'))  # Redirect to the contact details page
    else:
        form = ContactDetailForm(instance=contact_detail)

    return render(request, 'dashboard/admin_contact_detail_edit.html', {'form': form})

def admin_contact_messages(request):
    messages = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'dashboard/admin_contact_messages.html', {'messages': messages})

def ad_index(request):
    items = Index.objects.all()
    return render(request, 'dashboard/index/ad_index.html', {'index_items': items})

def edit_index_image(request, id):
    index = get_object_or_404(Index, id=id)

    if request.method == 'POST':
        if request.FILES.get('image'):
            index.image = request.FILES['image']
            index.save()
        return redirect('ad_index')  # Replace with your actual list view name

    return render(request, 'dashboard/index/edit_index_image.html', {'index': index})



def admin_rental_specs(request, id):
    rental = get_object_or_404(CarRentalRequest, id=id)
    specs = getattr(rental, 'specs', None)

    if request.method == 'POST':
        price_per_day = request.POST.get('price_per_day') or None
        mileage = request.POST.get('mileage') or None
        transmission = request.POST.get('transmission') or None
        seats = request.POST.get('seats') or None
        luggage_capacity = request.POST.get('luggage_capacity') or None

        if specs:
            # Update existing specs
            specs.price_per_day = price_per_day
            specs.mileage = mileage
            specs.transmission = transmission
            specs.seats = seats
            specs.luggage_capacity = luggage_capacity
            specs.save()
        else:
            # Create new specs
            specs = CarSpec.objects.create(
                rental=rental,
                price_per_day=price_per_day,
                mileage=mileage,
                transmission=transmission,
                seats=seats,
                luggage_capacity=luggage_capacity,
            )
        return redirect('admin_rental_requests')

    return render(request, 'dashboard/put_on_rent/specs.html', {
        'rental': rental,
        'specs': specs,
    })

from app.models import Booking, UserRentalBooking

def booking_dashboard(request):
    admin_bookings = Booking.objects.select_related('vehicle').order_by('-created_at')
    user_bookings = UserRentalBooking.objects.select_related('rental').order_by('-created_at')

    return render(request, 'dashboard/booking/booking.html', {
        'admin_bookings': admin_bookings,
        'user_bookings': user_bookings,
    })

from app.models import Testimonial  

def admin_testimonials(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'dashboard/testimonial/admin_testimonials.html', {'testimonials': testimonials})

def edit_testimonial(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            form.save()
            messages.success(request, 'Testimonial updated successfully.')
            return redirect('admin_testimonials')
    else:
        form = TestimonialForm(instance=testimonial)
    return render(request, 'dashboard/testimonial/edit_testimonial.html', {'form': form})

def delete_testimonial(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    testimonial.delete()
    messages.success(request, 'Testimonial deleted successfully.')
    return redirect('admin_testimonials')


def add_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Testimonial added successfully!")
            return redirect('admin_testimonials')
    else:
        form = TestimonialForm()
    return render(request, 'dashboard/testimonial/add_testimonial.html', {'form': form})

from app.models import Experience
from django.contrib import messages

def admin_counter(request):
    experience = Experience.objects.last()  # assuming one row

    if request.method == 'POST':
        experience.year_experienced = request.POST.get('year_experienced', 0)
        experience.total_cars = request.POST.get('total_cars', 0)
        experience.happy_customers = request.POST.get('happy_customers', 0)
        experience.total_branches = request.POST.get('total_branches', 0)
        experience.save()
        messages.success(request, 'Counter stats updated successfully!')
        return redirect('admin_counter')

    return render(request, 'dashboard/counter/admin_counter.html', {'experience': experience})


def ad_viewblog(request):
    blogs = Blog.objects.all().order_by('-published_date')
    return render(request, 'dashboard/blog/ad_viewblog.html', {'blogs': blogs})

def ad_addblog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user  # or assign author appropriately
            blog.save()
            messages.success(request, "Blog created successfully.")
            return redirect('ad_viewblog')
    else:
        form = BlogForm()

    context = {
        'form': form,
        'page_title': 'Add Blog',
        'submit_text': 'Create Blog',
    }
    return render(request, 'dashboard/blog/blog_form.html', context)


def ad_editblog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog updated successfully.")
            return redirect('ad_viewblog')
    else:
        form = BlogForm(instance=blog)

    context = {
        'form': form,
        'page_title': 'Edit Blog',
        'submit_text': 'Update Blog',
    }
    return render(request, 'dashboard/blog/blog_form.html', context)

def ad_deleteblog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        blog.delete()
        messages.success(request, "Blog deleted successfully.")
        return redirect('ad_viewblog')
    
    context = {
        'blog': blog,
    }
    return render(request, 'dashboard/blog/ad_deleteblog.html', context)