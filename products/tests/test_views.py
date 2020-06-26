from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from products.models import Product, Category, StockDrop


class TestProductViews(TestCase):

    def setUp(self):
        category = Category(name='clothing')
        category.save()
        valid_product = Product(name='A product',
                                category=category,
                                description='second string',
                                admin_tags=['this', 'is', 'an', 'array'],
                                price=10.99)
        valid_product.save()
        valid_stockdrop = StockDrop(name='SD1',
                                    description='description',
                                    image=SimpleUploadedFile(
                                        name='default.png',
                                        content=open(
                                            'media/default.png', 'rb').read(),
                                        content_type='image/jpeg',))
        valid_stockdrop.save()

    def test_query_returns_results(self):
        response = self.client.get('/?query=retro')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_list.html')

    def test_empty_query_returns_all_products(self):
        response = self.client.get('/?query=')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_list.html')
        with self.assertRaises(KeyError):
            self.assertTrue(response.context['stockdrops'])
        self.assertQuerysetEqual(response.context['products'],
                                 Product.objects.all().order_by('-date_added'),
                                 transform=lambda x: x)

    def test_render_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_list.html')
        self.assertTrue(response.context['products_active'])
        self.assertTrue(response.context['stockdrops'])
        self.assertQuerysetEqual(response.context['products'],
                                 Product.objects.all().order_by('-date_added'),
                                 transform=lambda x: x)

    def test_render_product_detail(self):
        valid_product = Product.objects.latest('date_added')
        response = self.client.get(f'/product/{valid_product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
        self.assertTrue(response.context['product'])
        self.assertTrue(response.context['categories_active'])

    def test_render_404_not_found(self):
        response = self.client.get('/product/0/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed('404.html')
