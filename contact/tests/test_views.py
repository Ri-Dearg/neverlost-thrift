from django.test import TestCase


class TestContactViews(TestCase):
    """Tests views for the Email app."""
    # Confirms the correct template is used
    def test_contact_template(self):
        self.client.get('/contact/')
        self.assertTemplateUsed('contact_form.html')
