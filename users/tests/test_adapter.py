import random
import string
from django.test import TestCase


def generate_string():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))


email = generate_string() + '@' + generate_string() + '.com'
password = generate_string()


class TestAdapter(TestCase):

    def test_redirect(self):
        new_user = {'username': generate_string(),
                    'email1': email,
                    'email2': email,
                    'password1': password,
                    'password2': password
                    }

        response = self.client.post('/accounts/signup/?next=/products/1/',
                                    new_user, follow=True)

        next = response.request['QUERY_STRING']

        self.assertEqual('next=/products/1/', next)
        self.assertEqual(response.status_code, 200)
