from django.urls import path
from home.api.views import *

urlpatterns = [
    path('pods/', PodListView.as_view(), name='pods'),
    path('pod-detail/<int:pk>/', PodDetailView.as_view(), name='pod-detail'),
]