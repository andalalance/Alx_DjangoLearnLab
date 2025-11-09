from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import UserProfile

class UserProfileModelTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.profile = UserProfile.objects.create(
            user=self.user,
            role='admin'
        )

    def test_user_profile_creation(self):
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertEqual(self.profile.role, 'admin')

    def test_user_profile_str(self):
        self.assertEqual(str(self.profile), 'testuser - admin')