from django.shortcuts import get_object_or_404

from products.models import Product


def get_cart(request):
    """Creates a cart context in the session and adds it to all pages."""
    cart = request.session.get('cart')
    cart_items = []
    cart_total = 0
    cart_quantity = 0

    if cart:
        cart_quantity += len(cart)
        for item_id, item_data in cart.items():
            product = get_object_or_404(Product, pk=item_id)
            cart_total += item_data * product.price
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })

    return {'cart': cart,
            'cart_quantity': cart_quantity,
            'cart_items': cart_items,
            'cart_total': cart_total}
