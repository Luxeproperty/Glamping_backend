from django.urls import include, path
from home.api.views import *



urlpatterns = [
    path('pods/', PodListView.as_view(), name='pods'),
    path('pod-detail/<int:pk>/', PodDetailView.as_view(), name='pod-detail'),
    path('images/', PodImageView.as_view(), name='images'),
    path('contact-us/', CreateContactView.as_view(), name='contact'),
    path('view-message', GetContactView.as_view(), name="view-message"),
    
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)