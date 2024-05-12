"""
This file contains tests for the Profiles app.
"""

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Profile


class ProfileModelTestCase(TestCase):
    """
    Tests to ensure that a profile can be created and linked to a user
    instance.
    """

    def setUp(self):
        """
        Creates a user and a password. Ensures a clean start for each test so
        that results aren't confused with previous tests data.
        """

        self.client = APIClient()
        self.test_user = User.objects.create_user(
            username="test_user",
            password="test_user_password",
        )
        Profile.objects.filter(owner=self.test_user).delete()

    def test_profile_creation(self):
        """
        Test logic for seeing if a profile has been created for the user.
        Initially checking the number of profiles, it tries to retrieve a
        profile that's associated with the user.  If one doesn't exist, it
        creates it it then checks the count again, and then checks that the
        new profile is correctly associated with the user.
        """
        initial_count = Profile.objects.count()
        profile, created = Profile.objects.get_or_create(
            owner=self.test_user,
        )
        new_count = Profile.objects.count()
        if created:

            self.assertEqual(new_count, initial_count + 1)

        self.assertEqual(profile.owner, self.test_user)
