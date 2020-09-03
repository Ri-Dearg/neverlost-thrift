from products.models import Product


def get_likes(request):
    """Creates a likes context in the session if anonymous, or from the
    UserProfile if logged in and adds it to all pages.
    Orders by last added item using a through table if logged in."""

    user = request.user
    likes = []

    # Uses likes from user profile if authenticated,
    # otherwise creates a session
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

    return {'likes': likes}
