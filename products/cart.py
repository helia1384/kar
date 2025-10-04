from django.shortcuts import get_object_or_404
from .models import Product
from django.shortcuts import redirect,render

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session['cart'] = cart
    return redirect('cart_view')

def cart_view(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0
    for product_id, qty in cart.items():
        product = get_object_or_404(Product, id=product_id)
        items.append({'product': product, 'qty': qty, 'subtotal': product.price * qty})
        total += product.price * qty
    return render(request, 'products/cart.html', {'items': items, 'total': total})

from django.shortcuts import redirect, get_object_or_404
from .models import Product

def update_cart(request, product_id, action):
    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart:
        if action == 'increase':
            cart[product_id] += 1
        elif action == 'decrease':
            cart[product_id] -= 1
            if cart[product_id] <= 0:
                del cart[product_id]

    request.session['cart'] = cart
    return redirect('cart_view')
