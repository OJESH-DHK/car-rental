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




