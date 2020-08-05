from django.test import TestCase

from contact.models import Email


class TestCheckoutModels(TestCase):

    def test_email_creation_and_string(self):
        email = {'email': 'test@test.com',
                 'name': 'fname lname',
                 'subject': 'interesting',
                 'message': 'this is a message'}

        self.client.post('/contact/', email)
        new_email = Email.objects.latest('date')
        self.assertTrue(new_email.message == 'this is a message')
        self.assertEqual(str(new_email), 'test@test.com, interesting')
