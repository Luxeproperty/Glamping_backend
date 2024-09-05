from django.urls import path
from home.views import AddPod

urlpatterns = [
    path('addpod', AddPod.as_view(), name='addpod'),
]