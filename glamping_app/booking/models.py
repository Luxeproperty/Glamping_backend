from django.db import models
from django.core.exceptions import ValidationError

from home.models import Pods

from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class GuestDetails(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    contact_number = PhoneNumberField(region="GB")
    email = models.EmailField(unique=True)
    post_code = models.CharField(max_length=10)
    country = CountryField(blank='(Select country)')
  
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Booking(models.Model):
    
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('arrived', 'Arrived'),
        ('departed', 'Departed'),
        ('completed', 'Completed'),
    ]
    
    pod = models.ForeignKey(Pods, on_delete=models.CASCADE)
    guest = models.ForeignKey(GuestDetails, on_delete=models.CASCADE)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    number_of_guests = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    
    def clean(self):
        if self.checkout_date <= self.checkin_date:
            raise ValidationError('Checkout date must be after checkin date')
    
        # Check if pod is already booked for this date range
        if Booking.objects.filter(
            pod = self.pod,
            checkin_date__lt = self.checkout_date,
            checkout_date__gt = self.checkin_date,
            status = "confirmed"
        ).exists():
            raise ValidationError('Pod is already booked for this date range')
        
    # Add if paid then status confirmed and if not then status pending
        
    def save(self, *args, **kwargs):
        self.clean()
        self.status = "confirmed"
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f'Booking for {self.guest} on {self.pod} from {self.checkin_date} to {self.checkout_date}'
    