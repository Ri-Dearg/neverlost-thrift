from django.contrib import messages

from config import settings
from products.models import Product

from decimal import Decimal


def get_cart(request):
    """Creates a cart context in the session and adds it to all pages.
    Checks details like quantity, stock, total cost as well as whether an item
    is invalid or not."""

    # Declares variables for use with the cart.
    cart = request.session.get('cart')
    cart_items = []
    cart_total = 0
    cart_quantity = 0

    if cart:
        # Creates a copy of the cart dictionary for iteration:
        temp_cart = cart.copy()
        for item_id, item_data in temp_cart.items():
            # Sets the total quantity of an item:
            cart_quantity += item_data

            # Confirms the item is valid or throws an error with a message:
            try:
                product = Product.objects.get(pk=item_id)
            except Product.DoesNotExist:
                # Declares product as false and removes it:
                product = False
                cart.pop(item_id)
                messages.warning(request,
                                 'A Product is unavailable.')

            # If the product is valid and in stock,
            # it calculates details for that item:
            if product is not False:
                if product.stock >= 1:
                    cart_total += item_data * product.price
                    cart_items.append({
                        'item_id': item_id,
                        'quantity': item_data,
                        'product': product})

                # Or else the item is removed from the cart with feedback:
                else:
                    cart.pop(item_id)
                    messages.warning(request,
                                     f'{product} has run out of stock!')

            # Skips the product if it is not False:
            else:
                pass

    # Checks the cart total price and declares delivery price accordingly.
    # The FREE_DELIVERY_THRESHOLD is a set price declared in settings.
    if cart_total < settings.FREE_DELIVERY_THRESHOLD and cart_total > 0:
        delivery = Decimal(settings.STANDARD_DELIVERY)
    else:
        delivery = 0

    # Calculates the grand total and then pushes all details into the context.
    grand_total = cart_total + delivery
    request.session.save()
    return {'cart': cart,
            'cart_quantity': cart_quantity,
            'cart_items': cart_items,
            'cart_total': cart_total,
            'delivery': delivery,
            'grand_total': grand_total}
