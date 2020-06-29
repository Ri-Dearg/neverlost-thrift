from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.views.generic import ListView

from django_ajax.decorators import ajax

from products.models import Product


class LikesListView(ListView):
    """View that displays all the liked products for the user."""
    model = Product
    context_object_name = 'products'
    template_name = 'likes/likes_list.html'


@ajax
def likes_toggle(request):
    """ Add an item to liked products"""

    if request.is_ajax and request.method == "POST":
        try:
            item_id = request.POST.get('item-id', '0')
            product = get_object_or_404(Product, pk=item_id)

            # Saves the item to the profile if the user is logged in, otherwise
            # saves to the session
            if request.user.is_authenticated:
                user = request.user
                liked_products = user.userprofile.liked_products

                if product in liked_products.all():
                    user.userprofile.liked_products.remove(product)
                    tag = 'info'
                    message = f'{product.name} unliked!'
                    result = 'unliked'
                else:
                    user.userprofile.liked_products.add(product)
                    tag = 'success'
                    message = f'{product.name} liked!'
                    result = 'liked'
            else:
                likes = request.session.get('likes', [])
                if item_id in likes:
                    likes.remove(item_id)
                    request.session['likes'] = likes
                    tag = 'info'
                    result = 'unliked'
                    message = f'{product.name} unliked!'
                else:
                    likes.append(item_id)
                    request.session['likes'] = likes
                    tag = 'success'
                    message = f'{product.name} liked!'
                    result = 'liked'
            return {'message': message, 'result': result, 'tag': tag}

        except Exception as e:
            result = 'error'
            tag = 'warning'
            message = f'Error liking item: {e}'
            return {'message': message, 'result': result, 'tag': tag}
