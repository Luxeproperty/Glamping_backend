from django.urls import path
from payment.api import views

app_name = "payment"

urlpatterns = [
    # path("create_payment/", views.PaymentView.as_view(), name="create_payment"),
    path("create_payment/<int:cart_id>/", views.PaymentView.as_view(), name="create_payment"),
] 