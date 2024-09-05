from rest_framework import serializers

from django_countries.serializer_fields import CountryField as CountryFieldSerializer

from booking.models import *


class GuestDetailSerializer(serializers.ModelSerializer):
    
    country = CountryFieldSerializer()
    
    class Meta:
        model = GuestDetails
        fields = '__all__'
        
    def create(self, validated_data):
        return GuestDetails.objects.create(**validated_data)
        

class BookingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Booking
        fields = '__all__'
        depth = 1
        

        