from django.test import TestCase


class TestContactViews(TestCase):

    def test_contact_template(self):
        self.client.get('/contact/')
        self.assertTemplateUsed('contact_form.html')
