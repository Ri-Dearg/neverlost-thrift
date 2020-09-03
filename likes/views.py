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
        """Adds all necessary information to the context.
        Gets likes from the account if the user is logged in,
        else it creates a list from the session to display the likes.
        Sorts the list in reverse chronological if the user is logged in.
        Finally it paginates for infinite scroll."""

        context = super().get_context_data(**kwargs)

        # Sets initial variables for the context
        user = self.request.user
        context['products'] = []

        # Adds liked products ffrom the account if logged in.
        if user.is_authenticated:
            liked_products = user.userprofile.liked_products.order_by(
                '-liked__datetime_added')
            for product in liked_products:
                context['products'].append(product)

        # Otherwise it creates a list of IDs and retrieves the products from
        # the DB before adding them to the context.
        else:
            id_list = []
            session_likes = self.request.session.get('likes')

            if session_likes:
                for key in session_likes:
                    id_list.append(key)
                liked_products = Product.objects.filter(id__in=id_list)

                for product in liked_products:
                    context['products'].append(product)

        # Paginates the items for the infinite scroll feed.
        products = context['products']
        paginator = Paginator(products, 9)

        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context


@ajax
def likes_toggle(request):
    """Add or removes the specified product to likes.
    The view is Ajaxed, so it is only called by a JS file.
    It checks whether the user is authenticated or anonymous and
    runs different functions accordingly.
    The decorator converts the response to JSON format.
    It is then picked up by the JS file which completes the page effects.
    'tag' and 'message' are used to display the toasts.
    'result' is used to define the logic on the JS side."""

    if request.is_ajax and request.method == "POST":
        # Runs through a number of variables to process the ajax call.
        # If it fails, it throws an exception with a message.
        try:
            item_id = request.POST.get('item-id')
            product = get_object_or_404(Product, pk=item_id)

            # Saves the item to the profile if the user is logged in, otherwise
            # saves to the session
            if request.user.is_authenticated:
                # Retrieves the User's liked products
                user = request.user
                liked_products = user.userprofile.liked_products

                # If the product is in the list it is unliked,
                # otherwise it is liked.
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
            
            # If the user is anonymous the items get added to the session.
            else:
                likes = request.session.get('likes', [])

                # If the product is in the list it is unliked,
                # otherwise it is liked.
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

        # If none of the conditions are true, it throws an error.
        except Exception as e:
            result = 'error'
            tag = 'warning'
            message = f'Error liking item: {e}'
        return {'message': message, 'result': result, 'tag': tag}


def update_likes(request):
    """This view is used to update the likes_popover.html template.
    It is called by the JS file after it successfully recieves
    the likes_toggle view response.
    It updates the context using the same logic as the get_likes context
    processor before refreshing the template.
    The JS script then pushes the newly rendered template into
    the popover HTML."""

    # Initialises a list for use with the context
    likes = []

    # Saves the item to the profile if the user is logged in, otherwise
    # saves to the session
    user = request.user
    if user.is_authenticated:
        liked_products = user.userprofile.liked_products.order_by(
            '-liked__datetime_added')
        for product in liked_products:
            likes.append(product)

    # Creates a list of IDs and retrieves the products from
    # the DB before adding them to the context.
    else:
        id_list = []
        session_likes = request.session.get('likes')

        if session_likes:
            for key in session_likes:
                id_list.append(key)
            liked_products = Product.objects.filter(id__in=id_list)

            for product in liked_products:
                likes.append(product)

    # Pushes the new context to the page before re-rendering the template.
    RequestContext(request).push({'likes': likes})
    return render(request, 'likes/includes/likes_popover.html')
