from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """
        Test creating a new user with an email is successful.
        """
        email = 'test@test.com'
        password = 'secretpass'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
        """
        Test the email is normalized
        """
        email = "test@FCGHVJKLJBHVBNM.com"
        user = get_user_model().objects.create_user(email,'test@123')

        self.assertEqual(user.email,email.lower())


    def test_new_user_invalid_email(self):
        """
        creating user with no email raises error
        """
        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_user(None, 'test@123')


    def test_new_super_user(self):
        """ test creating a new super user"""
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'test@123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)



