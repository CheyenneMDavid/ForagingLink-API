"""
This file contains tests for the Profiles app.
"""

from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
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


class ProfileUpdateTestCase(TestCase):
    """
    Tests to ensure that a profile can be updated.
    """

    def setUp(self):
        """
        Creates a user and a password with a profile and logs the user in.
        """

        self.client = APIClient()
        self.user = User.objects.create_user(
            username="test_user",
            password="test_password",
        )
        self.profile = Profile.objects.get(owner=self.user)
        self.client.login(username="test_user", password="test_password")

    def test_update_profile(self):
        """
        Tests if a profile is successfully updated.

        The test defines new data and sends it to the profile update endpoint.
        It then checks the response by refreshing the database and ensures
        that the profile's name and content
        have been updated correctly to "Updated Name" and "Updated Content",
        respectively.
        """

        # Prepares the URL for updating the profile using the profile's primary
        # key (pk)
        url = reverse("profile-detail", kwargs={"pk": self.profile.pk})

        # Defines the new data we want to update the profile with
        data = {"name": "Updated Name", "content": "Updated Content"}

        # Sends a PUT request to update the profile with the new data
        response = self.client.put(url, data)

        # Refreshes the profile from the database to get the updated values
        self.profile.refresh_from_db()

        # Checks if the server responded with a 200 OK which means that the
        # update was successful.
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifies that the profile's name has been updated correctly.
        self.assertEqual(self.profile.name, "Updated Name")

        # And verifies that the profile's content has been updated correctly
        self.assertEqual(self.profile.content, "Updated Content")
