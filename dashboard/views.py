from django.shortcuts import get_object_or_404, render, redirect
from app.models import (
    Vehicle, Index, TripRequest, AboutUs, Testimonial, Experience, 
    ServicesSection, ServicesOffered
)
from app.models import AboutUs
from django.contrib import messages

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard/base/admin_base.html')

def services(request):
    services_section = ServicesSection.objects.last()
    services_offered_list = ServicesOffered.objects.all()[:4]
    context = {
        'services_section': services_section,
        'services_offered_list': services_offered_list
    }
    return render(request,'dashboard/services/ad_services.html',context)


def add_service(request):
    if request.method == 'POST':
        service_name = request.POST.get('service_name')
        service_desc = request.POST.get('service_desc')

        if service_name and service_desc:
            ServicesOffered.objects.create(
                services_offered=service_name,
                services_offered_desc=service_desc
            )
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

def edit_service_offered(request, id):
    service_item = get_object_or_404(ServicesOffered, id=id)

    if request.method == 'POST':
        title = request.POST.get('services_offered')
        description = request.POST.get('services_offered_desc')

        service_item.services_offered = title
        service_item.services_offered_desc = description
        service_item.save()

        messages.success(request, "Service updated successfully.")
        return redirect('service')  

    context = {
        'service_item': service_item
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

def ad_about(request):
    about = AboutUs.objects.last()

    if request.method == "POST":
        about.title = request.POST.get("title")
        about.description = request.POST.get("description")

        if 'index_image' in request.FILES:
            about.index_image = request.FILES['index_image']
        if 'sub_image' in request.FILES:
            about.sub_image = request.FILES['sub_image']

        about.save()
        messages.success(request, "About section updated successfully.")
        return redirect('ad_about')

    context = {
        'about': about
    }
    return render(request, 'dashboard/about/ad_about.html', context)


