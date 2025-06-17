from django.db import models

class Feature(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Vehicle(models.Model):
    car_brand = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    features = models.ManyToManyField(Feature, blank=True)
    image = models.ImageField(upload_to='vehicles/')
    mileage = models.PositiveIntegerField( blank=True)
    transmission = models.CharField(max_length=50 , blank=True, choices=[
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
    ])
    seats = models.PositiveIntegerField()
    luggage_capacity = models.PositiveIntegerField(help_text="Luggage capacity in liters")

    def __str__(self):
        return f"{self.car_brand} {self.car_model}"

# to handle multiple admin added images
class VehicleImage(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='vehicle_images/')
    
class Index(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='index/')
    video_title = models.CharField(max_length=255, blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Index"
        ordering = ['title']


class TripRequest(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    pickup_location = models.CharField(max_length=100)
    dropoff_location = models.CharField(max_length=100)
    pickup_date = models.DateField()
    dropoff_date = models.DateField()
    pickup_time = models.TimeField()
    def __str__(self):
        return f"{self.full_name} - {self.phone}"



class AboutUs(models.Model):
    index_image = models.ImageField(upload_to='about_us/index_images/')
    sub_image = models.ImageField(upload_to='about_us/sub_images/')
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    person_image = models.ImageField(upload_to='testimonials/person_images/')
    testimonial = models.TextField()
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.position}"


class Experience(models.Model):
    year_experienced = models.PositiveIntegerField(default=0)
    total_cars = models.PositiveIntegerField(default=0)
    happy_customers = models.PositiveIntegerField(default=0)
    total_branches = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Counter"
        verbose_name_plural = "Counter"

    def __str__(self):
        return "Counter Stats"

class ServicesSection(models.Model):
    main_image = models.ImageField(upload_to='services/')
    second_image = models.ImageField(upload_to='services/')

    def __str__(self):
        return "Services Section"
        
class ServicesOffered(models.Model):
    services_offered = models.CharField(max_length=100, null=True, blank=True)
    services_offered_desc = models.CharField(max_length=100, null=True)
    def __str__(self):
        return "Services offered"
    
#Booking 
class Booking(models.Model):
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE, related_name='bookings')
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    pickup_date = models.DateField()
    return_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.vehicle.car_model}"


class CarRentalRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    car_brand = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    description = models.TextField()
    bluebook_image = models.ImageField(upload_to='bluebooks/')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.car_model} [{self.status}]"


class CarSpec(models.Model):
    rental = models.OneToOneField(CarRentalRequest, on_delete=models.CASCADE, related_name='specs')
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    mileage = models.PositiveIntegerField(blank=True, null=True)
    transmission = models.CharField(max_length=50, blank=True, null=True, choices=[
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
    ])
    seats = models.PositiveIntegerField(blank=True, null=True)
    luggage_capacity = models.PositiveIntegerField(blank=True, null=True, help_text="Luggage capacity in liters")

    def __str__(self):
        return f"Specs for {self.rental}"


class VehicleImage(models.Model):
    rental_request = models.ForeignKey(CarRentalRequest, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='vehicle_images/')



class ContactDetail(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return "Contact Detail"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
