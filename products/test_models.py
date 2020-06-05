from django.test import TestCase


class TestViews(TestCase):

    def test_render_index(self):
        page = self.client.get('/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed('index.html')
