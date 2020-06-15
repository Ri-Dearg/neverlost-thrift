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

    def test_error_on_incorrect_item_added(self):
        response = self.client.post('/cart/add/0/?next=/product/1/',
                                    {'quantity': '0'})

        self.assertRedirects(response, '/product/1/')
        self.assertRaises(Exception, msg='Error adding item: 0')

    def test_successfully_remove_from_cart(self):
        self.client.post('/cart/add/1/?next=/product/1/', {'quantity': '1'})
        session = self.client.session

        self.assertEqual(session['cart'], {'1': 1})

        response = self.client.post('/cart/remove/1/?next=/product/1/')

        session = self.client.session

        self.assertEqual(session['cart'], {})
        self.assertRedirects(response, '/product/1/')

    def test_error_on_incorrect_item_removed(self):
        response = self.client.post('/cart/add/1/?next=/product/1/',
                                    {'quantity': '1'})
        session = self.client.session

        self.assertEqual(session['cart'], {'1': 1})

        response = self.client.post('/cart/remove/0/?next=/product/1/')

        session = self.client.session

        self.assertRedirects(response, '/product/1/')
        self.assertRaises(Exception, msg='Error removing item: 0')
