import random
import string
from django.test import TestCase


def generate_string():
    """Creates a random string for use as a user"""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))


# Generates fake credentials
email = generate_string() + '@' + generate_string() + '.com'
password = generate_string()


class TestAdapter(TestCase):
    """A custom adapter was created, subclassing django-allauth's for a custom
    redirect. This tests the correct redirect."""

    def test_redirect(self):
        """Tests that the adapter redirects correctly."""
        # Creates a fake user
        new_user = {'username': generate_string(),
                    'email1': email,
                    'email2': email,
                    'password1': password,
                    'password2': password
                    }

        # Signs the user up with a redirect in the URL
        response = self.client.post('/accounts/signup/?next=/products/1/',
                                    new_user, follow=True)

        # Declares next as the query string
        next = response.request['QUERY_STRING']

        # Confirms the redirect is correct
        self.assertEqual('next=/products/1/', next)
        self.assertEqual(response.status_code, 200)
