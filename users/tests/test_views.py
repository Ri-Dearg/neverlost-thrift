from django.test import TestCase
from django.contrib.auth.models import User


class TestUserViews(TestCase):
    """Tests views for the Users app."""
    def setUp(self):
        """Creates a fake user for use in the tests."""
        username = 'user1'
        email = 'test@test.com'
        password = 'password'
        User.objects.get_or_create(username=username,
                                   email=email,
                                   password=password)

    def test_context(self):
        """Tests the all the correct context appear on the user's settings
        page. That's their shipping and billing info, emails, and custom info
        change forms"""

        # Retrieves the most recently created user, logs them in
        # and goes to their profile.
        test_user = User.objects.latest('date_joined')
        self.client.force_login(test_user)
        response = self.client.get(f'/users/profile/{test_user.id}/')

        # Confirms context for all required page items as stated in the above.
        self.assertTrue(response.context['user_profile_detail'])
        self.assertTrue(response.context['add_email_form'])
        self.assertTrue(response.context['change_password_form'])
        self.assertTrue(response.context['user'])
        self.assertTrue(response.context['profile'])

    def test_custom_email_view(self):
        """Confirms a custom view is used for changing email."""
        # Retrieves the most recently created user and logs them in
        test_user = User.objects.latest('date_joined')
        self.client.force_login(test_user)

        # Confirms a custom template is used
        self.client.get('/users/accounts/email/')
        self.assertTemplateUsed('users/user_detail.html')

    def test_custom_password_view(self):
        """Confirms a custom view is used for changing password."""
        # Retrieves the most recently created user and logs them in
        test_user = User.objects.latest('date_joined')
        self.client.force_login(test_user)

        # Confirms a custom template is used
        self.client.get('/users/accounts/password/change/')
        self.assertTemplateUsed('users/user_detail.html')

    def test_custom_update_shipping(self):
        """Confirms a custom view is used for changing email."""
        # Retrieves the most recently created user and logs them in
        test_user = User.objects.latest('date_joined')
        self.client.force_login(test_user)

        # Posts a valid form to update the info
        self.client.post('/users/shipping-billing/?next=/',
                         {'shipping_full_name': 'Test Name',
                          'shipping_phone_number_0': '+93',
                          'shipping_phone_number_1': '1',
                          'shipping_street_address_1': '',
                          'shipping_street_address_2': '',
                          'shipping_town_or_city': '',
                          'shipping_county': '',
                          'shipping_postcode': '424242',
                          'shipping_country': 'IE',
                          'billing_full_name': '',
                          'billing_phone_number_0': '+93',
                          'billing_phone_number_1': '1',
                          'billing_street_address_1': '',
                          'billing_street_address_2': '',
                          'billing_town_or_city': '',
                          'billing_county': '',
                          'billing_postcode': '',
                          'billing_country': 'IE'})

        # Confirms the name has been updated
        test_user = User.objects.latest('date_joined')
        self.assertEqual(test_user.userprofile.shipping_full_name,
                         'Test Name')
