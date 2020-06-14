from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(user_logged_in, sender=User)
def add_unsaved_likes_to_user(sender, user, request, **kwargs):
    """Transfer unauthenticated likes to User account"""
    session_likes = request.session.get('likes')
    if session_likes:
        user.userprofile.liked_products.add(*session_likes)
