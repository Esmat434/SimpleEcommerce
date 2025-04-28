from product.models import (
    Product
)

class Cart:
    def __init__(self,request):
        self.session = request.session

        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        
        self.cart = cart
    
    def add(self,product,quantity=1):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'price':product.price,'quantity':quantity}
        else:
            self.cart[product_id]['quantity']+=quantity if self.cart[product_id]['quantity'] < product.stock else 0
        
        self.session.modified = True
    
    def update(self,product,quantity):
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]['quantity'] = quantity
        
        self.session.modified = True

    def delete(self,product):
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True

    def get_products(self):
        product_ids = [int(product_id) for product_id in self.cart.keys()]

        products = Product.objects.prefetch_related('productimage_set').filter(id__in = product_ids)

        for product in products:
            product.quantity = int(self.cart[str(product.id)]['quantity'])

        return products
    
    def get_total_price(self):
        total_price = 0

        for item in self.cart.values():
            total_price+= float(item['price']) * int(item['quantity'])
        return total_price

    def __len__(self):
        return len(self.cart)