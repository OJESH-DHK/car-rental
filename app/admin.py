from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Vehicle, Feature, Index, TripRequest, Testimonial, AboutUs,
    Experience, ServicesSection, ServicesOffered, Booking, CarRentalRequest,
    VehicleImage, CarSpec, ContactDetail, ContactMessage
)

admin.site.register(Vehicle)
admin.site.register(CarSpec)
admin.site.register(Feature)
admin.site.register(Index)
admin.site.register(AboutUs)
admin.site.register(Testimonial)
admin.site.register(Experience)
admin.site.register(ServicesSection)
admin.site.register(ServicesOffered)
admin.site.register(Booking)
admin.site.register(UserRentalBooking)
@admin.register(VehicleImage)
class VehicleImageAdmin(admin.ModelAdmin):
    list_display = ('rental_request', 'image_tag')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 100px;"/>', obj.image.url)
        return "No Image"
    image_tag.short_description = 'Image Preview'


@admin.register(CarRentalRequest)
class CarRentalRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'car_model', 'car_brand', 'status', 'submitted_at')

@admin.register(TripRequest)
class TripRequestAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'phone',
        'pickup_location',
        'dropoff_location',
        'pickup_date',
        'dropoff_date',
        'pickup_time',
    )

admin.site.register(ContactDetail)
admin.site.register(ContactMessage)