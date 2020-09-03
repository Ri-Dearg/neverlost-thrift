from django.test import TestCase

from products.models import Product


class TestViews(TestCase):
    """Tests views for the Cart app."""
    def test_correct_template_used(self):
        """Checks that the url produces the correct template."""
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart_list.html')

    def test_confirm_add_to_cart_functions(self):
        """Tests add to cart functions, such as limiting stock,
        multiple items, updating quantities."""

        # Gets a product and sets a stock limit
        not_unique_product = Product.objects.get(pk=2)
        not_unique_product.is_unique = False
        not_unique_product.stock = 3
        not_unique_product.save()

        limit_stock_product = Product.objects.get(pk=1)
        limit_stock_product.stock = 5
        limit_stock_product.save()

        # Adds a normal quantity, then adds a quantity higher than the stock
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 2, 'quantity': '1'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 2, 'quantity': '4'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        # Updates the product when adding to cart
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 1, 'quantity': '10', 'special': 'update'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        # Confirms the quantity in cart is max stock.
        session = self.client.session
        self.assertEqual(session['cart'], {'1': 5, '2': 3})

    def test_error_on_incorrect_item_added(self):
        """Adds an invalid item to the cart and confirms that an error is
        raised."""

        # Adds a non-existaet item and confirms an error
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 0, 'quantity': '0'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertRaises(Exception, msg='Error adding item: 0')

        # Adds an item with no stock and confirms an error.
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
        """Tests that the ajax toggle first adds an item and
        then removes the item from the cart."""

        # This adds the item
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 1, 'quantity': '1'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        session = self.client.session

        # confirms the item is in the cart
        self.assertEqual(session['cart'], {'1': 1})

        # This removes the item
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 1, 'quantity': '1'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        session = self.client.session

        # Confirms the cart is now empty
        self.assertEqual(session['cart'], {})

    def test_error_on_incorrect_item_removed(self):
        """Checks that an error occurs in the toggle when an
        item isn't in the cart"""

        # This adds the item
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 1, 'quantity': '1'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        session = self.client.session

        # confirms the item is in the cart
        self.assertEqual(session['cart'], {'1': 1})

        # Uses the toggle on a non-existant item
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 0, 'quantity': '0'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        # confirms the error message
        self.assertRaises(Exception, msg='Error removing item: 0')

    def test_update_cart_view(self):
        """Tests numerous functions relating to updating the cart update view,
        mainly to ensure that the context information is correct."""

        # Tests the template is updated when the view is called
        self.client.get('/cart/update/')
        self.assertTemplateUsed('cart/includes/cart_popover.html')

        # This adds the item
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 2, 'quantity': '1'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        # Declares an invalid item inside the cart
        session = self.client.session
        session['cart'] = {'2': 1, '0': 0}
        session.save()

        # Confirms that it cannot update the cart with an invalid item.
        self.client.get('/cart/update/')
        self.assertRaises(Exception, msg='Error adding item: 0')

        # Declares an item with no stock
        no_stock_product = Product.objects.get(pk=1)
        no_stock_product.stock = 0
        no_stock_product.save()

        # Adds an item with no stock
        self.client.post('/cart/ajax/toggle/',
                         {'item-id': 1, 'quantity': '1'},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        # Ensures the item is not added to the cart on update
        self.client.get('/cart/update/')
        session = self.client.session
        self.assertEqual(session['cart'], {'2': 1})

    def test_refresh_total_view_template(self):
        """Confirms the correct template is used for the cart list page."""
        self.client.get('/cart/totals/')
        self.assertTemplateUsed('cart/includes/totals.html')
