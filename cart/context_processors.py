from django.contrib import messages

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
        temp_cart = cart.copy()
        for item_id, item_data in temp_cart.items():
            cart_quantity += item_data
            try:
                product = Product.objects.get(pk=item_id)
            except Product.DoesNotExist:
                product = False
                cart.pop(item_id)
                messages.warning(request,
                                 'A Product is unavailable.')
            if product is not False:
                if product.stock > 0:
                    cart_total += item_data * product.price
                    cart_items.append({
                        'item_id': item_id,
                        'quantity': item_data,
                        'product': product})
                else:
                    cart.pop(item_id)
                    messages.warning(request,
                                     f'{product} has run out of stock!')
            else:
                pass

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
