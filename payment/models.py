from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product
# Create your models here.

User = get_user_model()

class ShippingAddress(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50,blank=True)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255,blank=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=6)

    def __str__(self):
        return self.username

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(ShippingAddress,on_delete=models.CASCADE)
    total_price = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20,choices=[('pending','Pending'),('paid','Paid')])
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()

class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    order = models.OneToOneField(Order,on_delete=models.CASCADE)
    cart_number = models.CharField(max_length=20)
    cart_holder = models.CharField(max_length=150)
    expiry_date = models.DateField()
    cvv = models.CharField(max_length=4)
    amount = models.PositiveIntegerField(default=0)
    paid = models.BooleanField(default=False)
    trnasaction_id = models.CharField(max_length=100,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
