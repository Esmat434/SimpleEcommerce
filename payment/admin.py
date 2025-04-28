from django.contrib import admin
from .models import (
    ShippingAddress,Order,OrderItem,Payment
)
# Register your models here.

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['user','username','email','address1','country','city','zipcode']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','shipping_address','total_price','status']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order','product','quantity','price']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user','order','cart_number','cvv','amount','paid']