from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from products.models import Product


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    next = request.GET.get('next', '')
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        # cart[item_id] += quantity
        # messages.success(request, f'Updated {product.name} quantity to \
        #     {cart[item_id]}')
        pass
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    return HttpResponseRedirect(next)
