from django.urls import path
from home.api.views import *

urlpatterns = [
    path('pods/', PodListView.as_view(), name='pods'),
    path('pod-detail/<int:pk>/', PodDetailView.as_view(), name='pod-detail'),
    path('images/', PodImageView.as_view(), name='images'),
    path('contact-us/', CreateContactView.as_view(), name='contact'),
    path('view-message', GetContactView.as_view(), name="view-message")
]