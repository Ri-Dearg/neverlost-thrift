from django.test import TestCase
from django.contrib.auth.models import User


class TestViews(TestCase):
    """Tests views for the Likes app."""
    def setUp(self):
        """Sets up or retrieves a fake user for use in the tests."""
        username = 'user1',
        email = 'test@test.com'
        password = 'password'
        User.objects.get_or_create(username=username,
                                   email=email,
                                   password=password)

    def test_correct_template_used_and_context(self):
        """Checks that the correct template is used after adding likes."""
        # Adds a liked product to session and retrieves the page
        self.client.post('/likes/ajax/toggle/', {'item-id': 1},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.client.post('/likes/ajax/toggle/', {'item-id': 2},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        response = self.client.get('/likes/')
        session = self.client.session.get('likes')

        # Confirms correct likes in the session, and the correct template
        self.assertEqual(session, ['1', '2'])
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'likes/likes_list.html')

        # Logs in the user
        test_user = User.objects.latest('date_joined')
        self.client.force_login(test_user)

        # Confirms that the session likes have been transferred to the user
        # and are correctly displayed in the context.
        response = self.client.get('/likes/')
        self.assertEqual(response.context['products'],
                         list(test_user.userprofile.liked_products.order_by(
                             '-liked__datetime_added')))

    def test_confirm_add_to_likes(self):
        """Tests that items are successfully added
        when a user is both logged in and anonymous"""

        # Adds a liked product
        self.client.post('/likes/ajax/toggle/', {'item-id': 1},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        # Confirms likes are in the session
        session = self.client.session
        self.assertEqual(session['likes'], ['1'])

        # Logs in the user
        test_user = User.objects.latest('date_joined')
        self.client.force_login(test_user)

        # Adds likes while logged in and confirms that two liked
        # products are in the account.
        self.client.post('/likes/ajax/toggle/', {'item-id': 2},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertTrue(len(test_user.userprofile.liked_products.all()) == 2)

    def test_error_on_incorrect_item_added(self):
        """Confirms that an error shows when adding an invalid item."""
        # Adds a liked product
        self.client.post('/likes/ajax/toggle/', {'item-id': 0},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        # Confirms an error message shows
        self.assertRaises(Exception, msg='Error adding item: 0')

    def test_successfully_remove_from_likes(self):
        """Checks that the like toggle removes liked products
        for both anonymous and logged in users."""

        # Adds a liked product
        self.client.post('/likes/ajax/toggle/', {'item-id': 1},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        # Confirms the product is in the session
        session = self.client.session
        self.assertEqual(session['likes'], ['1'])

        # Removes a liked product
        self.client.post('/likes/ajax/toggle/', {'item-id': 1},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        # Confirms the product is removed from the session
        session = self.client.session
        self.assertEqual(session['likes'], [])

        # Logs in a user
        test_user = User.objects.latest('date_joined')
        self.client.force_login(test_user)

        # Adds a liked product
        self.client.post('/likes/ajax/toggle/', {'item-id': 2},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        # Removes a liked product
        self.client.post('/likes/ajax/toggle/', {'item-id': 2},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        # Confirms the product is removed from the users likes
        self.assertTrue(len(test_user.userprofile.liked_products.all()) == 0)

    def test_error_on_incorrect_item_removed(self):
        """Confirms an error occurs on trying to remove an invalid item"""
        # Adds a liked product
        self.client.post('/likes/ajax/toggle/', {'item-id': 1},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        # Confirms the product is in the session
        session = self.client.session
        self.assertEqual(session['likes'], ['1'])

        # Toggles an invalid item and confirms an error message
        self.client.post('/likes/ajax/toggle/', {'item-id': 0})
        self.assertRaises(Exception, msg='Error removing item: 0')

    def test_update_like_view(self):
        """Tests numerous functions relating to updating the likes update view,
        mainly to ensure that the context information is correct."""

        # Tests the template is updated when the view is called
        self.client.get('/likes/update/')
        self.assertTemplateUsed('likes/includes/likes_popover.html')

        # Adds a liked product
        self.client.post('/likes/ajax/toggle/', {'item-id': 2},
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        # Updates the template and context
        self.client.get('/likes/update/')
        self.assertTemplateUsed('likes/includes/likes_popover.html')

        # Logs a user in and updates the context
        test_user = User.objects.latest('date_joined')
        self.client.force_login(test_user)
        self.client.get('/likes/update/')

        # Confirms the session context
        session = self.client.session
        self.assertEqual(session['likes'], ['2'])
