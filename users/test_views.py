from django.test import TestCase
from django.contrib.auth.models import User

from .models import UserProfile


class TestUserViews(TestCase):

    def setUp(self):

        username = 'user1',
        email = 'test@test.com'
        password = 'password'
        User.objects.get_or_create(username=username,
                                           email=email,
                                           password=password)

    def test_context(self):
        print
        test_user = User.objects.latest('date_joined')
        self.client.force_login(test_user)
        response = self.client.get(f'/users/profile/{test_user.id}/')

        self.assertTrue(response.context['field_names'])
        self.assertTrue(response.context['values'])
        self.assertTrue(response.context['user'])
        self.assertTrue(response.context['profile'])
