from django.test import TestCase
from .models import Product


class TestViews(TestCase):

    def test_render_index(self):
        page = self.client.get('/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed('product_list.html')
        self.assertQuerysetEqual(page.context['products'],
                                 Product.objects.all().order_by('-date_added'))
