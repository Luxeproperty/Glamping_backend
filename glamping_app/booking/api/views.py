from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView

from booking.models import GuestDetails, Booking

from booking.api.serializers import GuestDetailSerializer, BookingSerializer

from django.shortcuts import get_object_or_404
from django.http import Http404


class CreatGuestView(APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = GuestDetailSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
        queryset = GuestDetails.objects.all()
        serializer = GuestDetailSerializer(queryset, many=True)
        return Response(serializer.data)
    

class GuestView(APIView):
    
    def get(self, request, pk, *args, **kwargs):
        try:
            guest = get_object_or_404(GuestDetails, pk=pk)
            serializer = GuestDetailSerializer(guest)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Http404:
            return Response({"error": "Guest not found."}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk, *args, **kwargs):
        
        try:
            guest = get_object_or_404(GuestDetails, pk=pk)
            serializer = GuestDetailSerializer(guest, data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            return Response({"error": "Guest not found."}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk, *args, **kwargs):
        
        try:
            guest = get_object_or_404(GuestDetails, pk=pk)
            guest.delete()
            return Response({"message": "Guest deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response({"error": "Guest not found."}, status=status.HTTP_404_NOT_FOUND)
        


class CreateBookingView(APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = BookingSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
        
        bookings = Booking.objects.filter(status="confirmed")
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class BookingView(APIView):
    
    def get(self, request, pk, *args, **kwargs):
        
        try:
            booking = get_object_or_404(Booking, pk=pk)
            serializer = BookingSerializer(booking)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Http404:
            return Response({"error": "Booking not found."}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk, *args, **kwargs):
        
        try:
            booking = get_object_or_404(Booking, pk=pk)
            serializer = BookingSerializer(booking, data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            return Response({"error": "Booking not found."}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk, *args, **kwargs):
        
        try:
            booking = get_object_or_404(Booking, pk=pk)
            booking.status = "available"
            booking.delete()
            return Response({
                "message": "Booking deleted successfully.",
                },
                status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response({"error": "Booking not found."}, status=status.HTTP_404_NOT_FOUND)
        

        