from django.apps import apps
from django.test import TestCase
from users.apps import UsersConfig


class TestUsersConfig(TestCase):

    def test_app(self):
        self.assertEqual('users', UsersConfig.name)
        self.assertEqual('users', apps.get_app_config('users').name)
