from django.urls import path
from .views import (
    cart_summary,cart_add,cart_update_quantity,cart_delete
)

urlpatterns = [
    path('cart/',cart_summary,name='cart'),
    path('cart_add/',cart_add,name='cart_add'),
    path('cart_update_quantity/',cart_update_quantity,name='cart_update_quantity'),
    path('cart_delete/',cart_delete,name='cart_delete'),
]