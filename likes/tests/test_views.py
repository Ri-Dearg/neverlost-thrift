from django.test import TestCase
from django.contrib.auth.models import User


class TestViews(TestCase):

    def setUp(self):

        username = 'user1',
        email = 'test@test.com'
        password = 'password'
        User.objects.get_or_create(username=username,
                                   email=email,
                                   password=password)

    def test_confirm_add_to_likes(self):
        response = self.client.post('/likes/add/1/?next=/product/1/')
        session = self.client.session

        self.assertRedirects(response, '/product/1/')
        self.assertEqual(session['likes'], [1])

        test_user = User.objects.latest('date_joined')
        self.client.force_login(test_user)
        response = self.client.post('/likes/add/2/?next=/product/1/')
        self.assertTrue(len(test_user.userprofile.liked_products.all()) == 2)

    def test_error_on_incorrect_item_added(self):
        response = self.client.post('/likes/add/0/?next=/product/1/',
                                    )

        self.assertRedirects(response, '/product/1/')
        self.assertRaises(Exception, msg='Error adding item: 0')

    def test_successfully_remove_from_likes(self):
        self.client.post('/likes/add/1/?next=/product/1/', )
        session = self.client.session

        self.assertEqual(session['likes'], [1])

        response = self.client.post('/likes/remove/1/?next=/product/1/')
        session = self.client.session

        self.assertEqual(session['likes'], [])
        self.assertRedirects(response, '/product/1/')

        test_user = User.objects.latest('date_joined')
        self.client.force_login(test_user)
        self.client.post('/likes/add/2/?next=/product/1/')
        self.client.post('/likes/remove/2/?next=/product/1/')
        self.assertTrue(len(test_user.userprofile.liked_products.all()) == 0)

    def test_error_on_incorrect_item_removed(self):
        response = self.client.post('/likes/add/1/?next=/product/1/',
                                    )
        session = self.client.session

        self.assertEqual(session['likes'], [1])

        response = self.client.post('/likes/remove/0/?next=/product/1/')

        session = self.client.session

        self.assertRedirects(response, '/product/1/')
        self.assertRaises(Exception, msg='Error removing item: 0')
