import stripe

from django.conf import settings
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from booking.models import Booking
from booking.api.serializers import BookingSerializer
from booking.api.views import BookingView

from payment.models import Payment

class PaymentView(APIView):
    
    def post(self, request, pk, *args, **kwargs):
        booking = get_object_or_404(Booking, pk=pk)
        token = request.data.get('stripe_token')
        amount = 1000
        
        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                source=token,
                description='Payment for cart {}'.format(booking.id),
            )
            
            payment = Payment.objects.create(
                booking=booking,
                amount=amount,
                stripe_charge_id = charge.id
            )
            
            booking.status = "confirmed"
            booking.save()
            return Response({'message': 'Payment successful'}, status=status.HTTP_202_ACCEPTED)
            
        except:
            booking.status = "pending"
            return Response({'message': 'Payment failed'}, status=status.HTTP_400_BAD_REQUEST)