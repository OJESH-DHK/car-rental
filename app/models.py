from django.db import models

# Create your models here.
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
    pickup_location = models.CharField(max_length=200)
    dropoff_location = models.CharField(max_length=200)
    pickup_date = models.DateField()
    dropoff_date = models.DateField()
    pickup_time = models.TimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pickup_location} to {self.dropoff_location} on {self.pickup_date}"


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






