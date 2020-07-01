import random
import string

from django.test import TestCase
from django.contrib.auth.models import User

from products.models import Product
from users.models import Liked


class TestUserProfile(TestCase):

    def setUp(self):
        def generate_string():
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
        user1 = User.objects.latest('date_joined')
        user_string = str(user1.userprofile)

        liked_table = Liked.objects.get(userprofile=user1.userprofile)
        liked_string = str(liked_table)
        product = Product.objects.latest('date_added')
        self.assertEqual((user_string), (user1.username))
        self.assertEqual((liked_string),
                         (f'{user1.username}, {product.name}, {liked_table.datetime_added}')) # noqa E501

    def test_readable_fields(self):
        user1 = User.objects.latest('date_joined')
        result1, result2 = user1.userprofile._readable_field()

        self.assertEqual((result1[0]), ('shipping name'))
        self.assertEqual((result2[0]), 'Fake name')
