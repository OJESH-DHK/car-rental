from django.db import models

# Create your models here.
from django.db import models

class Vehicle(models.Model):
    car_brand = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='vehicles/')
    mileage = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    features = models.TextField(
        help_text="Comma-separated features like: Air Conditioning, Bluetooth, GPS",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.car_brand} {self.car_model}"

    @property
    def name(self):
        return f"{self.car_brand} {self.car_model}"
