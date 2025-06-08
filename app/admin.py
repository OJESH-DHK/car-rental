from django.contrib import admin
from .models import Vehicle, Feature, Index,TripRequest, Testimonial, AboutUs, Experience, ServicesSection, ServicesOffered

admin.site.register(Vehicle)
admin.site.register(Feature)
admin.site.register(Index)
admin.site.register(TripRequest)
admin.site.register(AboutUs)
admin.site.register(Testimonial)
admin.site.register(Experience)
admin.site.register(ServicesSection)
admin.register(ServicesOffered)
