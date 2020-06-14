def get_likes(request):

    user = request.user

    if user.is_authenticated:
        likes = []
        liked_products = user.userprofile.liked_products.all()
        for product in liked_products:
            likes.append(product.id)
    else:
        likes = request.session.get('likes')

    return {'likes': likes}
