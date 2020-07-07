import re

from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from products.models import Product, Category, StockDrop


class ProductTests(TestCase):
    """
    Tests for Product models
    """

    def setUp(self):
        category = Category(name='clothing', friendly_name='Clothing')
        category.save()

        valid_stockdrop = StockDrop(name='SD1',
                                    description='description',
                                    image=SimpleUploadedFile(
                                        name='default.png',
                                        content=open(
                                            'media/default.png', 'rb').read(),
                                        content_type='image/jpeg',))
        valid_stockdrop.save()

    def test_categories_str(self):
        self.assertEqual(str(Category.objects.get(pk=1)), ('clothing'))

    def test_products_str(self):
        test_name = Product(name='A product', price=10.99)
        self.assertEqual(str(test_name), ('A product: €10.99'))

    def test_product_image_file_is_processed_correctly(self):
        new_product = Product.objects.latest(
            'date_added')
        new_product.image = SimpleUploadedFile(
            name='default.png',
            content=open('media/default.png', 'rb').read(),
            content_type='image/jpeg')
        new_product.save()
        self.assertEqual(new_product.image.height, 500)
        self.assertEqual(new_product.image.width, 500)
        self.assertTrue(re.search('^product_images/default.*.png$',
                                  new_product.image.name))

    def test_product_does_not_save_duplicate_image(self):
        old_product = Product.objects.get(pk=1)
        old_product.save()
        self.assertEqual(old_product.image.name,
                         'product_images/default_yR7lhBQ.png')

    def test_stockdrop_image_file_is_processed_correctly(self):
        sd1 = StockDrop.objects.latest('date_added')
        sd1.image = SimpleUploadedFile(
            name='default.png',
            content=open('media/default.png', 'rb').read(),
            content_type='image/jpeg')
        new_stockdrop = StockDrop.objects.latest('date_added')
        new_stockdrop.save()
        self.assertEqual(new_stockdrop.image.height, 480)
        self.assertEqual(new_stockdrop.image.width, 1280)
        self.assertTrue(re.search('^stock_drop/default.*.png$',
                                  new_stockdrop.image.name))

    def test_stockdrop_str(self):
        sd1 = StockDrop.objects.latest('date_added')
        self.assertEqual(str(sd1),
                         (f'{sd1.date_added.strftime("%B")}: {sd1.name}'))
