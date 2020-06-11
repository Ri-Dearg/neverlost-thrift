from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from products.models import Product


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    next = request.GET.get('next', '')
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        # bag[item_id] += quantity
        # messages.success(request, f'Updated {product.name} quantity to \
        #     {bag[item_id]}')
        pass
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return HttpResponseRedirect(next)
