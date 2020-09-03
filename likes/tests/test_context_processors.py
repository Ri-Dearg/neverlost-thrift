from django.test import TestCase
from django.contrib.auth.models import User


class TestContext(TestCase):
    """Tests the context processor orders likes correctly in the template."""
    def setUp(self):
        """Creates a user and adds likes to their account."""
        username = 'user1',
        email = 'test@test.com'
        password = 'password'
        User.objects.get_or_create(username=username,
                                   email=email,
                                   password=password)
        test_user = User.objects.latest('date_joined')
        test_user.userprofile.liked_products.add(*[1, 2, 3])

    def test_likes_list_creation(self):
        """Creates a list in the same manner as the context processor
        and checks that it is equal to the context."""

        # Logs in the user from the setup view
        test_user = User.objects.latest('date_joined')
        self.client.force_login(test_user)
        response = self.client.get('/')

        # Creates a fake list based on the user's likes and
        # orders it like the context does
        test_list = []
        for product in test_user.userprofile.liked_products.all().order_by(
                '-liked__datetime_added'):
            test_list.append(product)

        # Confirms the context and the test list display the same.
        self.assertEqual(response.context['likes'],
                         test_list)
        self.assertTrue(len(test_user.userprofile.liked_products.all()) == 3)
