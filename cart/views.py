from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.template import RequestContext

from django_ajax.decorators import ajax

from config import settings
from products.models import Product

from decimal import Decimal


class CartListView(ListView):
    """View that displays all the products in the cart."""
    model = Product
    context_object_name = 'products'
    template_name = 'cart/cart_list.html'


@ajax
def cart_toggle(request):
    """Add a quantity of the specified product to the shopping cart."""

    if request.is_ajax and request.method == "POST":
        try:
            item_id = request.POST.get('item-id', '0')
            product = get_object_or_404(Product, pk=item_id)
            quantity = int(request.POST.get('quantity'))
            cart = request.session.get('cart', {})

            if item_id in list(cart.keys()):
                cart.pop(str(item_id))
                request.session['cart'] = cart
                tag = 'info'
                message = f'Removed {product.name} from your cart.'
                result = 'uncarted'

                # cart[item_id] += quantity
            # messages.success(request, f'Updated {product.name} quantity to \
                #     {cart[item_id]}')
            else:
                cart[item_id] = quantity
                request.session['cart'] = cart
                tag = 'success'
                message = f'Added {product.name} to your cart.'
                result = 'carted'

        except Exception as e:
            result = 'error'
            tag = 'warning'
            message = f'Error adding item to cart: {e}'

        return {'message': message, 'result': result, 'tag': tag}


def update_cart(request):
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

    if cart_total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = Decimal(settings.STANDARD_DELIVERY)
    else:
        delivery = 0

    grand_total = cart_total + delivery

    RequestContext(request).push({'cart': cart,
                                  'cart_quantity': cart_quantity,
                                  'cart_items': cart_items,
                                  'cart_total': cart_total,
                                  'delivery': delivery,
                                  'grand_total': grand_total})

    return render(request, 'cart/includes/cart_popover.html')


def refresh_total(request):
    print(request)
    return render(request, 'cart/includes/totals.html')
