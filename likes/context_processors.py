from products.models import Product


def get_likes(request):
    """Creates a like context in the session and adds it to all pages."""
    user = request.user

    likes = []

    # Uses likes from user profile if authenticated,
    # otherwise creates a session
    if user.is_authenticated:
        liked_products = user.userprofile.liked_products.order_by(
            '-liked__datetime_added')
        for product in liked_products:
            likes.append(product)
    else:
        id_list = []
        session_likes = request.session.get('likes')

        for key in session_likes:
            id_list.append(key)
        liked_products = Product.objects.filter(id__in=id_list)

        for product in liked_products:
            likes.append(product)

    return {'likes': likes}
