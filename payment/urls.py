from django.urls import path
from .views import (
    shipping_register,payment_view,payment_success_view
)

urlpatterns = [
    path('shipping/',shipping_register,name='shipping'),
    path('payment/<int:order_id>/',payment_view,name='payment'),
    path('payment_success/',payment_success_view,name='payment_success')
]