from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.template import RequestContext
from django.contrib import messages

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

            if request.POST.get('special') == 'update':
                cart[item_id] = quantity
                if cart[item_id] > product.stock:
                    cart[item_id] = product.stock
                request.session['cart'] = cart
                tag = 'success'
                message = f'Updated {product.name} quantity to \
                    {cart[item_id]}.'
                result = 'uncarted'

            elif (item_id in list(cart.keys()) and product.is_unique) or (
                    request.POST.get('special') == 'remove'):
                cart.pop(str(item_id))
                request.session['cart'] = cart
                tag = 'info'
                message = f'Removed {product.name} from your cart.'
                result = 'uncarted'

            elif item_id in list(cart.keys()) and not product.is_unique:
                cart[item_id] += quantity
                if cart[item_id] > product.stock:
                    cart[item_id] = product.stock
                request.session['cart'] = cart
                tag = 'success'
                message = f'Updated {product.name} quantity to \
                    {cart[item_id]}.'
                result = 'uncarted'
            else:
                cart[item_id] = quantity
                if cart[item_id] > product.stock:
                    cart[item_id] = product.stock
                request.session['cart'] = cart
                tag = 'success'
                message = f'Added {product.name} to your cart.'
                result = 'carted'

        except Exception as e:
            result = 'error'
            tag = 'warning'
            message = f'Error adding item to cart: {e}'

        if 'special' in request.POST:
            special = request.POST.get('special')
            return {'message': message, 'result': result, 'tag': tag,
                    'special': special}
        else:
            return {'message': message, 'result': result, 'tag': tag}


def update_cart(request):
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
                if product.stock >= 1:
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
    request.session.save()

    RequestContext(request).push({'cart': cart,
                                  'cart_quantity': cart_quantity,
                                  'cart_items': cart_items,
                                  'cart_total': cart_total,
                                  'delivery': delivery,
                                  'grand_total': grand_total})

    return render(request, 'cart/includes/cart_popover.html')


def refresh_total(request):
    return render(request, 'cart/includes/totals.html')
