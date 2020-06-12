from django.test import TestCase


class TestViews(TestCase):

    def test_confirm_add_to_cart(self):
        response = self.client.post('/cart/add/1/?next=/product/1/',
                                    {'quantity': '1'})
        session = self.client.session

        self.assertRedirects(response, '/product/1/')
        self.assertEqual(session['cart'], {'1': 1})

    def test_item_can_only_be_added_once(self):
        self.client.post('/cart/add/1/?next=/products/1',
                         {'quantity': '1'})
        self.client.post('/cart/add/1/?next=/products/1',
                         {'quantity': '1'})

        session = self.client.session
        self.assertEqual(session['cart'], {'1': 1})
