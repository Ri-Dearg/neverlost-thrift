from django.test import TestCase

from products.models import Product


class TestViews(TestCase):

    def test_correct_template_used(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart_list.html')

    def test_confirm_add_to_cart(self):
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 1, 'quantity': '1'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        session = self.client.session

        self.assertEqual(session['cart'], {'1': 1})

    def test_error_on_incorrect_item_added(self):
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 0, 'quantity': '0'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertRaises(Exception, msg='Error adding item: 0')

        no_stock_product = Product.objects.get(pk=1)
        no_stock_product.stock = 0
        no_stock_product.save()
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 1, 'quantity': '1'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        session = self.client.session
        self.client.get('/')
        self.assertEqual(session['cart'], {})

        self.assertRaises(Exception, msg='Error adding item: 0')

    def test_successfully_remove_from_cart(self):
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 1, 'quantity': '1'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        session = self.client.session

        self.assertEqual(session['cart'], {'1': 1})

        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 1, 'quantity': '1'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        session = self.client.session

        self.assertEqual(session['cart'], {})

    def test_error_on_incorrect_item_removed(self):
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 1, 'quantity': '1'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        session = self.client.session

        self.assertEqual(session['cart'], {'1': 1})

        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 0, 'quantity': '0'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        session = self.client.session

        self.assertRaises(Exception, msg='Error removing item: 0')
