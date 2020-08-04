from django.test import TestCase
from django.contrib.messages import get_messages
from django.contrib.auth.models import User

from checkout.models import Order

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

    def setUp(self):

        username = 'user1',
        email = 'test@test.com'
        password = 'password'
        User.objects.get_or_create(username=username,
                                   email=email,
                                   password=password)

    def test_order_creation_and_detail_view(self):
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 1, 'quantity': '1'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 2, 'quantity': '2'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.client.get('/checkout/')
        self.assertTemplateUsed('order_form.html')

        global valid_order_dict
        self.client.post('/checkout/', valid_order_dict)

        new_order = Order.objects.latest('date')
        self.assertEqual(new_order.billing_full_name, 'Jeremy Fisher')

        my_order = self.client.session['my_order']
        self.assertTrue(my_order)
        self.client.get(f'/checkout/order/{new_order.id}/')
        self.assertTemplateUsed('order_detail.html')

    def test_shipping_and_billing_connect(self):
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 2, 'quantity': '2'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.client.get('/checkout/')
        global valid_billing_order
        self.client.post('/checkout/', valid_billing_order)

        new_order = Order.objects.latest('date')
        self.assertEqual(new_order.shipping_full_name, 'Jeremy Fisher')

    def test_order_detail_view_after_login(self):
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 1, 'quantity': '1'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 2, 'quantity': '2'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        test_user = User.objects.latest('date_joined')
        self.client.force_login(test_user)
        global valid_order_dict
        self.client.post('/checkout/', valid_order_dict)

        new_order = Order.objects.latest('date')
        self.client.get(f'/checkout/order/{new_order.id}/')
        self.assertTemplateUsed('order_detail.html')

    def test_order_list_view_after_login(self):
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 1, 'quantity': '1'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 2, 'quantity': '2'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        test_user = User.objects.latest('date_joined')
        self.client.force_login(test_user)
        global valid_order_dict
        self.client.post('/checkout/', valid_order_dict)

        self.client.get('/checkout/orders/')
        self.assertTemplateUsed('order_list.html')

    def test_invalid_form_message(self):

        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 1, 'quantity': '1'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        response = self.client.post('/checkout/', {'full_name': 'whatever'})

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'There was a problem processing the order. Please double check your information.') # noqa E501

    def test_empty_cart_returns_redirect(self):
        response = self.client.get('/checkout/')

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'The cart is empty.')
        self.assertRedirects(response, '/')

    def test_order_removes_invalid_item(self):
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 1, 'quantity': '1'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        session = self.client.session
        session['cart'] = {'1': 1, '2': 3, '0': 1}
        session.save()
        global valid_order_dict
        self.client.post('/checkout/', valid_order_dict)
        new_order = Order.objects.latest('date')
        self.assertEqual(new_order.original_cart, '{"1": 1, "2": 3}')
