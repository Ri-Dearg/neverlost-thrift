from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.views.generic import ListView

from django_ajax.decorators import ajax

from products.models import Product


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
