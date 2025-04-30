import uuid

from accounts.decorators import login_required

from cart.cart import Cart

from product.models import Product

from django.shortcuts import render,redirect,get_object_or_404

from .forms import (
    ShippingAddressCreationForm,PaymentCreationForm
)

from .models import (
    ShippingAddress,Payment,Order,OrderItem
)

@login_required
def shipping_register_view(request):
    cart = request.session.get('sesssion_key',{})
    if not cart or not any(cart.items()):
        return redirect('cart')
    
    try:
        shipping = ShippingAddress.objects.get(user = request.user)
        order = order_add(request)
        return redirect('payment',order.id)
    except:
        if request.method == 'POST':
            form = ShippingAddressCreationForm(request.POST)
            if form.is_valid():
                shipping = form.save(commit=False)
                shipping.user = request.user
                shipping.save()
                order = order_add(request)
                return redirect('payment',order.id)
    form = ShippingAddressCreationForm()
    return render(request,'shipping.html',{'form':form})

def order_add(request):
    shipping_address = get_object_or_404(ShippingAddress,user = request.user)

    order = Order.objects.create(
        user = request.user,
        shipping_address = shipping_address
    )
    return order

def orderItem_add(request,order):
    cart = Cart(request)
    cart_data = request.session.get('session_key',{})

    for product_id,item in cart_data.items():
        product = get_object_or_404(Product,id = int(product_id))
        price = int(item['price'])
        quantity = int(item['quantity'])
        product.stock-=quantity
        product.save()

        OrderItem.objects.create(
            order = order,
            product = product,
            quantity = quantity,
            price = price
        )
    order.total_price = cart.get_total_price()
    order.save()

@login_required
def payment_view(request,order_id):
    order = get_object_or_404(Order,id = order_id, user = request.user)
    if request.method == 'POST':
        form = PaymentCreationForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.order = order
            payment.amount = order.total_price
            payment.paid = True
            payment.transaction_id = str(uuid.uuid4())
            payment.save()
            orderItem_add(request,order)
            request.session['session_key'] = {}
            request.session.modified = True
            return redirect('payment_success')
    form = PaymentCreationForm()
    return render(request,'payment.html',{'form':form})

@login_required
def payment_success_view(request):
    return render(request,'payment_success.html')