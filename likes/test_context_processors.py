from django.test import TestCase
from django.contrib.auth.models import User


class TestContext(TestCase):

    def setUp(self):

        username = 'user1',
        email = 'test@test.com'
        password = 'password'
        User.objects.get_or_create(username=username,
                                   email=email,
                                   password=password)
        test_user = User.objects.latest('date_joined')
        test_user.userprofile.liked_products.add(*[1, 2, 3])

    def test_likes_list_creation(self):
        test_user = User.objects.latest('date_joined')
        self.client.force_login(test_user)
        response = self.client.get('/')

        self.assertEqual(response.context['likes'], [3, 2, 1])
        self.assertTrue(len(test_user.userprofile.liked_products.all()) == 3)
