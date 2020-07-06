from django.shortcuts import get_object_or_404

from config import settings
from products.models import Product

from decimal import Decimal


def get_cart(request):
    """Creates a cart context in the session and adds it to all pages."""
    cart = request.session.get('cart')
    cart_items = []
    cart_total = 0
    cart_quantity = 0

    if cart:
        for item_id, item_data in cart.items():
            cart_quantity += item_data
            product = get_object_or_404(Product, pk=item_id)
            cart_total += item_data * product.price
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })

    if cart_total < settings.FREE_DELIVERY_THRESHOLD and cart_total > 0:
        delivery = Decimal(settings.STANDARD_DELIVERY)
    else:
        delivery = 0

    grand_total = cart_total + delivery

    return {'cart': cart,
            'cart_quantity': cart_quantity,
            'cart_items': cart_items,
            'cart_total': cart_total,
            'delivery': delivery,
            'grand_total': grand_total}
