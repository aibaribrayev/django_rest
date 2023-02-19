"""
Tests for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an phone_number is successful."""
        phone_number = '+77777777777'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            phone_number=phone_number,
            password=password,
        )

        self.assertEqual(user.phone_number, phone_number)
        self.assertTrue(user.check_password(password))

