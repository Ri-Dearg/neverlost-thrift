import random
import string

from django.test import TestCase

from .models import UserProfile, User


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
        user1.userprofile.default_shipping_name = 'Fake name'
        user1.userprofile.save()

    def test_str(self):
        user1 = User.objects.latest('date_joined')
        user_string = str(user1.userprofile)
        self.assertEqual((user_string), (user1.username))

    def test_readable_fields(self):
        user1 = User.objects.latest('date_joined')
        result1, result2 = user1.userprofile.readable_field()

        self.assertEqual((result1[0]), ('default shipping name'))
        self.assertEqual((result2[0]), 'Fake name')
