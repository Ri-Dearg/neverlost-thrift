import re

from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Product, Category

category = Category(name='clothing', friendly_name='Clothing')
category.save()
valid_product = Product(name='A product',
                        category=category,
                        description='a string',
                        admin_tags=['this', 'is', 'an', 'array'],
                        price=10.99)


class ProductTests(TestCase):
    """
    Tests for Product models
    """
    valid_product.save()

    def test_str(self):
        test_name = Product(name='A product', price=10.99)
        self.assertEqual(str(test_name), ('A product: €10.99'))

    def test_image_file_is_processed_correctly(self):
        valid_product.image = SimpleUploadedFile(
            name='default.png',
            content=open('media/default.png', 'rb').read(),
            content_type='image/jpeg')
        new_product = Product.objects.latest('date_added')
        self.assertEqual(new_product.image.height, 500)
        self.assertEqual(new_product.image.width, 500)
        self.assertTrue(re.search('^product_images/default.*.png$',
                                  new_product.image.name))
