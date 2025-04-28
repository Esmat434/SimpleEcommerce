from django.urls import path
from .views import (
    product_list,product_detail,rate_product
)

urlpatterns = [
    path('',product_list,name='product_list'),
    path('product/<slug:slug>/',product_detail,name='product_detail'),
    path('rate_product/',rate_product,name='rate_product'),
]