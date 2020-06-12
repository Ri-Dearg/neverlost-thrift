from django.test import TestCase
from .models import Product, Category

category = Category(name='clothing')
category.save()
valid_product = Product(name='A product',
                        category=category,
                        description='second string',
                        admin_tags=['this', 'is', 'an', 'array'],
                        price=10.99)


class TestViews(TestCase):

    valid_product.save()

    def test_render_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('product_list.html')
        self.assertTrue(response.context['products_active'])
        self.assertQuerysetEqual(response.context['products'],
                                 Product.objects.all().order_by('-date_added'),
                                 transform=lambda x: x)

    def test_render_product_detail(self):
        response = self.client.get(f'/product/{valid_product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('product_detail.html')
        self.assertTrue(response.context['product'])
        self.assertTrue(response.context['categories_active'])

    def test_render_404_not_found(self):
        response = self.client.get('/product/0/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed('404.html')
