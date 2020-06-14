from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.views.generic import ListView

from products.models import Product


class CartListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'cart/cart_list.html'


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    next = request.GET.get('next', '')

    try:
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
    except Exception as e:
        messages.error(request, f'Error adding item: {e}')
        return HttpResponseRedirect(next)


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    next = request.GET.get('next', '')

    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})

        cart.pop(str(item_id))
        messages.success(request, f'Removed {product.name} from your cart')

        request.session['cart'] = cart
        return HttpResponseRedirect(next)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponseRedirect(next)
