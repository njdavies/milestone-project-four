from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from products.models import Product


def view_cart(request):
    """
    A View that renders the cart contents page
    """
    return render(request, 'cart.html')


def add_to_cart(request, item_id):
    """
    Add an item to the cart
    """
    quantity = 1

    cart = request.session.get('cart', {})
    if item_id in cart:
        cart[item_id] = int(cart[item_id]) + quantity
    else:
        cart[item_id] = cart.get(item_id, quantity)

    request.session['cart'] = cart
    messages.success(request, 'Item added to cart')
    return redirect(reverse('products'))


def remove_from_cart(request, item_id):
    """
    Remove an item from the cart
    """
    cart = request.session.get('cart', {})
    cart.pop(item_id)
    request.session['cart'] = cart
    messages.success(request, 'Item removed from cart')
    return redirect(reverse('view_cart'))
