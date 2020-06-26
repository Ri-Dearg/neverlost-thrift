def get_likes(request):
    """Creates a like context in the session and adds it to all pages."""
    user = request.user

    # Uses likes from user profile if authenticated,
    # otherwise creates a session
    if user.is_authenticated:
        likes = []
        liked_products = user.userprofile.liked_products.order_by(
            '-liked__datetime_added')
        for product in liked_products:
            likes.append(product.id)
    else:
        likes = request.session.get('likes')

    return {'likes': likes}
