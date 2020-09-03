import random
import string

from django.test import TestCase
from django.contrib.auth.models import User

from products.models import Product
from users.models import Liked


class TestUserProfile(TestCase):
    """Tests the models for the Users app."""
    def setUp(self):
        """Creates a newly signed up user and declares some profile details."""
        def generate_string():
            """Creates a random string for use as a user"""
            return ''.join(random.choices(string.ascii_uppercase +
                                          string.digits,
                                          k=8))

        username = generate_string(),
        email = generate_string() + '@' + generate_string() + '.com'
        password = generate_string()
        user1 = User.objects.create(username=username,
                                    email=email,
                                    password=password)
        user1.userprofile.shipping_name = 'Fake name'
        user1.userprofile.liked_products.set([Product.objects.latest(
            'date_added').id])
        user1.userprofile.save()

    def test_str(self):
        """Tests the string method on the UserProfile."""
        # Retrieves the most recently created user and gets their string
        user1 = User.objects.latest('date_joined')
        user_string = str(user1.userprofile)

        # Retrieves the user's liked products and gets its string
        liked_table = Liked.objects.get(userprofile=user1.userprofile)
        liked_string = str(liked_table)
        product = Product.objects.latest('date_added')

        # Cofirms the userprofile string is correct.
        self.assertEqual((user_string), (user1.username))

        # Confirms the User's Liked Product string is correct.
        self.assertEqual((liked_string),
                         (f'{user1.username}, {product.name}, {liked_table.datetime_added}'))  # noqa E501
