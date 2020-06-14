from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.views.generic import ListView

from products.models import Product


class LikesListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'likes/likes_list.html'


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
            likes = request.session.get('likes', [])
            likes.append(item_id)

            request.session['likes'] = likes
            messages.success(request, f'{product.name} liked!')
        return HttpResponseRedirect(next)

    except Exception as e:
        messages.error(request, f'Error liking item: {e}')
        return HttpResponseRedirect(next)
