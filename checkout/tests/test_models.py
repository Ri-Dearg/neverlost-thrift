from django.test import TestCase

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


class TestCheckoutModels(TestCase):

    def test_order_and_lineitem_string(self):
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 1, 'quantity': '1'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        global valid_order_dict
        self.client.post('/checkout/', valid_order_dict)
        new_order = Order.objects.latest('date')
        order_lineitem = new_order.lineitems.get(product=1)

        self.assertEqual(str(new_order), new_order.order_number)
        self.assertEqual(str(order_lineitem),
                         f'{order_lineitem.product.name} on order {new_order.order_number}') # noqa E501
