from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.contrib import messages

from products.models import Product


def add_to_likes(request, item_id):
    """ Add an item to liked products"""

    next = request.GET.get('next', '')

    try:
        product = get_object_or_404(Product, pk=item_id)
        if request.user.is_authenticated:
            user = request.user
            user.userprofile.liked_products.add(product)
            messages.success(request, f'{product.name} liked!')
        else:
            liked = request.session.get('liked', [])
            liked.append(item_id)

            request.session['liked'] = liked
            messages.success(request, f'{product.name} liked!')
        return HttpResponseRedirect(next)

    except Exception as e:
        messages.error(request, f'Error liking item: {e}')
        return HttpResponseRedirect(next)
