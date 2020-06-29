from django.test import TestCase
from django.contrib.messages import get_messages

from checkout.models import Order, OrderLineItem

valid_order_dict = {
        'full_name': 'Jeremy Fisher',
        'email': 'test@test.com',
        'phone_number_0': '+353',
        'phone_number_1': '891111111',
        'country': 'IE',
        'town_or_city': 'Location',
        'street_address_1': 'location at place',
    }


class TestCheckoutViews(TestCase):

    def test_order_creation(self):
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

        self.assertEqual(new_order.full_name, 'Jeremy Fisher')

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

    def test_order_error_on_adding_invalid_item(self):
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 1, 'quantity': '1'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        session = self.client.session
        session['cart'] = {'1': 1, '0': 0}
        session.save()

        global valid_order_dict
        self.client.post('/checkout/', valid_order_dict)
        new_order = Order.objects.latest('date')
        with self.assertRaises(OrderLineItem.DoesNotExist):
            new_order.lineitems.get(product=0)
