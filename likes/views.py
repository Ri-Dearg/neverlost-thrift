from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.views.generic import ListView

from products.models import Product


class LikesListView(ListView):
    """View that displays all the liked products for the user."""
    model = Product
    context_object_name = 'products'
    template_name = 'likes/likes_list.html'


def add_to_likes(request, item_id):
    """ Add an item to liked products"""

    # Used for redirection
    next = request.GET.get('next', '')

    try:
        product = get_object_or_404(Product, pk=item_id)
        # Saves the item to the profile if the user is logged in, otherwise
        # saves to the session
        if request.user.is_authenticated:
            user = request.user
            user.userprofile.liked_products.add(product)

            messages.success(request, f'{product.name} liked!')
        else:
            likes = request.session.get('likes', [])
            likes.append(item_id)
            request.session['likes'] = likes

            messages.success(request, f'{product.name} liked!')
        return HttpResponseRedirect(next)

    except Exception as e:
        messages.warning(request, f'Error liking item: {e}')
        return HttpResponseRedirect(next)


def remove_from_likes(request, item_id):
    """Remove the item from the shopping cart"""

    # Used for redirection
    next = request.GET.get('next', '')

    try:
        product = get_object_or_404(Product, pk=item_id)
        # Removes the item from the profile if the user is logged in, otherwise
        # removes from the session
        if request.user.is_authenticated:
            user = request.user
            user.userprofile.liked_products.remove(product)

            messages.warning(request, f'{product.name} unliked!')
        else:
            likes = request.session.get('likes', [])
            likes.remove(item_id)
            request.session['likes'] = likes

            messages.warning(request, f'{product.name} unliked!')
        return HttpResponseRedirect(next)

    except Exception as e:
        messages.warning(request, f'Error unliking item: {e}')
        return HttpResponseRedirect(next)
