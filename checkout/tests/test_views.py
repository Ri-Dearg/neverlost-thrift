from django.test import TestCase
from django.contrib.messages import get_messages
from django.contrib.auth.models import User

from checkout.models import Order

# Declares a dictionary to send in forms with valid data for an Order
valid_order_dict = {
    'shipping_full_name': 'Jeremy Fisher',
    'email': 'test@test.com',
    'shipping_phone_number_0': '+353',
    'shipping_phone_number_1': '891111111',
    'shipping_country': 'IE',
    'shipping_town_or_city': 'Location',
    'shipping_street_address_1': 'location at place',
    'billing_full_name': 'Jeremy Fisher',
    'billing_phone_number_0': '+353',
    'billing_phone_number_1': '891111111',
    'billing_country': 'IE',
    'billing_town_or_city': 'Location',
    'billing_street_address_1': 'location at place',
    'client_secret': '_secret_test'
}

# Used to check billing and shipping info connect by sending the checkbox.
# All the information must be sent in a test as the Javascript is inactive.
valid_billing_order = {
    'shipping_full_name': 'Jeremy Fisher',
    'email': 'test@test.com',
    'shipping_phone_number_0': '+353',
    'shipping_phone_number_1': '891111111',
    'shipping_country': 'IE',
    'shipping_county': 'Kerry',
    'shipping_postcode': '42424',
    'shipping_town_or_city': 'Location',
    'shipping_street_address_1': 'location at place',
    'shipping_street_address_2': 'Other place',
    'billing_full_name': '11',
    'billing_phone_number_0': '+353',
    'billing_phone_number_1': '891111111',
    'billing_country': 'IE',
    'billing_town_or_city': '1',
    'billing_street_address_1': '1',
    'client_secret': '_secret_test',
    'billing-same': 'on'
}


class TestCheckoutViews(TestCase):
    """Tests views for the Checkout app."""
    def setUp(self):
        """Sets up or retrieves a fake user for use in the tests."""
        username = 'user1',
        email = 'test@test.com'
        password = 'password'
        User.objects.get_or_create(username=username,
                                   email=email,
                                   password=password)

    def test_order_creation_and_detail_view(self):
        """Checks all the basic functions of the checkout app,
        order creation, templates used and correct information"""

        # Adds items to the cart
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 1, 'quantity': '1'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 2, 'quantity': '2'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        # Checks the correct template is used
        self.client.get('/checkout/')
        self.assertTemplateUsed('order_form.html')

        # Sends valid form data to create the order
        global valid_order_dict
        self.client.post('/checkout/', valid_order_dict)

        # Checks the order is created with the correct info
        new_order = Order.objects.latest('date')
        self.assertEqual(new_order.billing_full_name, 'Jeremy Fisher')

        # Retrieves the order and confirms the correct template is used
        # This checks without a login, using session storage
        my_order = self.client.session['my_order']
        self.assertTrue(my_order)
        self.client.get(f'/checkout/order/{new_order.id}/')
        self.assertTemplateUsed('order_detail.html')

    def test_order_detail_view_after_login(self):
        """Runs the same test as the preceding view but logs in a user."""
        # Adds items to the cart
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 1, 'quantity': '1'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 2, 'quantity': '2'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        # Retrives the user created in the setup view, logs them in
        # and creates an order
        test_user = User.objects.latest('date_joined')
        self.client.force_login(test_user)
        global valid_order_dict
        self.client.post('/checkout/', valid_order_dict)

        # Confirms the user can still view the order detail page
        new_order = Order.objects.latest('date')
        self.client.get(f'/checkout/order/{new_order.id}/')
        self.assertTemplateUsed('order_detail.html')

    def test_shipping_and_billing_connect(self):
        """Tests that the shipping info overrides the billing info if the box
        is ticked that they are the same."""

        # This adds the item to the cart
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 2, 'quantity': '2'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        # Send the order info with the billing-same checkbox
        self.client.get('/checkout/')
        global valid_billing_order
        self.client.post('/checkout/', valid_billing_order)

        # Retrieves the order and confirms
        # the Billing name has been overwritten.
        new_order = Order.objects.latest('date')
        self.assertEqual(new_order.shipping_full_name, 'Jeremy Fisher')

    def test_order_list_view_after_login(self):
        """Tests that a logged in user can view their order history."""
        # Adds items to the cart
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 1, 'quantity': '1'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 2, 'quantity': '2'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        # Retrives the user created in the setup view, logs them in
        # and creates an order
        test_user = User.objects.latest('date_joined')
        self.client.force_login(test_user)
        global valid_order_dict
        self.client.post('/checkout/', valid_order_dict)

        # Confirms the User can view their order history list
        self.client.get('/checkout/orders/')
        self.assertTemplateUsed('order_list.html')

    def test_invalid_form_message(self):
        """Tests a message is sent if invalid form information is posted."""
        # Adds items to the cart
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 1, 'quantity': '1'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        # Posts incomplete form info
        response = self.client.post('/checkout/', {'full_name': 'whatever'})

        # Confirms a suitable response message is sent.
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'There was a problem processing the order. Please double check your information.')  # noqa E501

    def test_empty_cart_returns_redirect(self):
        """Tests that going to the checkout with an empty cart
        will redirect you to the homepage"""

        # Goes to checkout with an empty cart
        response = self.client.get('/checkout/')

        # Check for an approriate message and the redirect to the homepage
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'The cart is empty.')
        self.assertRedirects(response, '/')

    def test_order_removes_invalid_item(self):
        """Tests that if an order contains an invalid item,
        the item is removed from the order."""

        # Adds items to the cart
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 1, 'quantity': '1'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        # Declares an invalid item in the cart
        session = self.client.session
        session['cart'] = {'1': 1, '2': 3, '0': 1}
        session.save()

        # Creates an order.
        global valid_order_dict
        self.client.post('/checkout/', valid_order_dict)

        # Retrieves the order, confirming the invalid item has not been added
        new_order = Order.objects.latest('date')
        self.assertEqual(new_order.original_cart, '{"1": 1, "2": 3}')
