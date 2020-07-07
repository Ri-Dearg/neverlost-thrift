from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.template import RequestContext


from django_ajax.decorators import ajax

from products.models import Product


class LikesListView(ListView):
    """View that displays all the liked products for the user."""
    model = Product
    context_object_name = 'products'
    template_name = 'likes/likes_list.html'

    def get_context_data(self, **kwargs):
        """Adds all necessary information to the context"""
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['products'] = []

        if user.is_authenticated:
            liked_products = user.userprofile.liked_products.order_by(
                '-liked__datetime_added')
            for product in liked_products:
                context['products'].append(product)
        else:
            id_list = []
            session_likes = self.request.session.get('likes')

            if session_likes:
                for key in session_likes:
                    id_list.append(key)
                liked_products = Product.objects.filter(id__in=id_list)

                for product in liked_products:
                    context['products'].append(product)

        products = context['products']
        paginator = Paginator(products, 9)

        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context


@ajax
def likes_toggle(request):
    """ Add an item to liked products"""

    if request.is_ajax and request.method == "POST":
        try:
            item_id = request.POST.get('item-id')
            product = get_object_or_404(Product, pk=item_id)

            # Saves the item to the profile if the user is logged in, otherwise
            # saves to the session
            if request.user.is_authenticated:
                user = request.user
                liked_products = user.userprofile.liked_products

                if product in liked_products.all():
                    user.userprofile.liked_products.remove(product)
                    product.save()
                    tag = 'info'
                    message = f'{product.name} unliked!'
                    result = 'unliked'
                else:
                    user.userprofile.liked_products.add(product)
                    product.save()
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

        except Exception as e:
            result = 'error'
            tag = 'warning'
            message = f'Error liking item: {e}'
        return {'message': message, 'result': result, 'tag': tag}


def update_likes(request):
    likes = []

    user = request.user
    if user.is_authenticated:
        liked_products = user.userprofile.liked_products.order_by(
            '-liked__datetime_added')
        for product in liked_products:
            likes.append(product)
    else:
        id_list = []
        session_likes = request.session.get('likes')

        if session_likes:
            for key in session_likes:
                id_list.append(key)
            liked_products = Product.objects.filter(id__in=id_list)

            for product in liked_products:
                likes.append(product)

    RequestContext(request).push({'likes': likes})
    return render(request, 'likes/includes/likes_popover.html')
