from django.test import TestCase
from .models import Product


class ProductTests(TestCase):
    """
    Tests for Product models
    """

    def test_str(self):
        test_name = Product(name='A product', price=10.99)
        self.assertEqual(str(test_name), ('A product, 10.99'))
