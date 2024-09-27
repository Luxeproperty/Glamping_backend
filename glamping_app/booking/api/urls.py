from django.urls import path
from booking.api.views import *

urlpatterns = [
    path('register/', CreatGuestView.as_view(), name='register'),
    path('guest/<int:pk>/', GuestView.as_view(), name='guest'),
    path('create_booking/', CreateBookingView.as_view(), name='create_booking'),
    path('view_booking/<int:pk>/', BookingView.as_view(), name='view_booking')
]