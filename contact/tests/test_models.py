from django.test import TestCase

from contact.models import Email


class TestCheckoutModels(TestCase):
    """Tests the models for the checkout app."""
    def test_email_creation_and_string(self):
        """Tests the string method for the model."""
        # A valid email dictionary
        email = {'email': 'test@test.com',
                 'name': 'fname lname',
                 'subject': 'interesting',
                 'message': 'this is a message'}

        # Posts the email, retrieves the email object and confirms the string
        self.client.post('/contact/', email)
        new_email = Email.objects.latest('date')
        self.assertTrue(new_email.message == 'this is a message')
        self.assertEqual(str(new_email), 'test@test.com, interesting')
