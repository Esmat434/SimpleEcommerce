from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from product.models import (
    Product
)
from .cart import Cart
# Create your views here.

def cart_summary(request):
    cart = Cart(request)

    products = cart.get_products()
    total_price = cart.get_total_price()
    return render(request,'cart.html',{'products':products,'total_price':total_price})

def cart_add(request):
    cart = Cart(request)
    if request.method == 'POST':
        product_id = request.POST.get('product_id')

        product = get_object_or_404(Product,id = int(product_id))

        cart.add(product)
        total_cart = cart.__len__()
        return JsonResponse({'total_cart':total_cart})

def cart_update_quantity(request):
    cart = Cart(request)
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')

        product = get_object_or_404(Product,id = product_id)

        cart.update(product,quantity)
        total_price = cart.get_total_price()
        return JsonResponse({'success':'quantity of item success updated','total_price':total_price})

def cart_delete(request):
    cart = Cart(request)
    if request.method == 'POST':
        product_id = request.POST.get('product_id')

        product = get_object_or_404(Product,id = int(product_id))

        cart.delete(product)
        total_price = cart.get_total_price()
        return JsonResponse({'success':f'{product.name} sucessfully deleted.','total_price':total_price})