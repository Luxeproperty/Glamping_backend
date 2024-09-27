from django.db import models
from booking.models import Booking
# Create your models here.

class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    stripe_charge_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)
