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

    def test_correct_template_used_and_context(self):
        self.client.post('/likes/ajax/toggle/', {'item-id': 1},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.client.post('/likes/ajax/toggle/', {'item-id': 2},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        response = self.client.get('/likes/')
        session = self.client.session.get('likes')
        self.assertEqual(session, ['1', '2'])
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'likes/likes_list.html')

        test_user = User.objects.latest('date_joined')
        self.client.force_login(test_user)
        response = self.client.get('/likes/')
        self.assertEqual(response.context['products'],
                         list(test_user.userprofile.liked_products.order_by(
                             '-liked__datetime_added')))

    def test_confirm_add_to_likes(self):
        self.client.post('/likes/ajax/toggle/', {'item-id': 1},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        session = self.client.session

        self.assertEqual(session['likes'], ['1'])

        test_user = User.objects.latest('date_joined')
        self.client.force_login(test_user)
        self.client.post('/likes/ajax/toggle/', {'item-id': 2},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertTrue(len(test_user.userprofile.liked_products.all()) == 2)

    def test_error_on_incorrect_item_added(self):
        self.client.post('/likes/ajax/toggle/', {'item-id': 0},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertRaises(Exception, msg='Error adding item: 0')

    def test_successfully_remove_from_likes(self):
        self.client.post('/likes/ajax/toggle/', {'item-id': 1},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        session = self.client.session

        self.assertEqual(session['likes'], ['1'])

        self.client.post('/likes/ajax/toggle/', {'item-id': 1},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        session = self.client.session

        self.assertEqual(session['likes'], [])

        test_user = User.objects.latest('date_joined')
        self.client.force_login(test_user)
        self.client.post('/likes/ajax/toggle/', {'item-id': 2},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.client.post('/likes/ajax/toggle/', {'item-id': 2},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertTrue(len(test_user.userprofile.liked_products.all()) == 0)

    def test_error_on_incorrect_item_removed(self):
        self.client.post('/likes/ajax/toggle/', {'item-id': 1},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        session = self.client.session

        self.assertEqual(session['likes'], ['1'])

        self.client.post('/likes/ajax/toggle/', {'item-id': 0})

        session = self.client.session

        self.assertRaises(Exception, msg='Error removing item: 0')

    def test_update_like_view(self):
        self.client.get('/likes/update/')
        self.assertTemplateUsed('likes/includes/likes_popover.html')

        self.client.post('/likes/ajax/toggle/', {'item-id': 2},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.client.get('/likes/update/')
        self.assertTemplateUsed('likes/includes/likes_popover.html')

        test_user = User.objects.latest('date_joined')
        self.client.force_login(test_user)
        self.client.get('/likes/update/')

        session = self.client.session

        self.assertEqual(session['likes'], ['2'])
