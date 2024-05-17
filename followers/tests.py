from django.test import TestCase
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from .models import Follower


class FollowerModelTest(TestCase):
    """
    Test case for the Follower model to ensure that a follower relationship
    can be created between two users and that it is unique.
    """

    def setUp(self):
        """
        Set up test data for the tests.

        Creates two users and a follower relationship between them for testing
        purposes.
        """
        self.user1 = User.objects.create_user(
            username="test_user_1",
            password="test_password_1",
        )
        self.user2 = User.objects.create_user(
            username="test_user_2",
            password="test_password_2",
        )
        self.follower = Follower.objects.create(
            owner=self.user1,
            followed=self.user2,
        )

    def test_follower_creation(self):
        """
        Tests the creation of the follower relationship.

        Verifies that the follower relationship is correctly created with the
        expected owner and followed users and then checks that the instance is
        of the Follower model and its string representation.
        """
        self.assertEqual(self.follower.owner, self.user1)
        self.assertEqual(self.follower.followed, self.user2)
        self.assertTrue(isinstance(self.follower, Follower))
        self.assertEqual(str(self.follower), f"{self.user1} {self.user2}")

    def test_unique_together(self):
        """
        Tests that the relationship is unique.

        Ensures that any attempts to create a duplicate relationship
        between the same users, raises an IntegrityError.
        """
        with self.assertRaises(IntegrityError):
            Follower.objects.create(
                owner=self.user1,
                followed=self.user2,
            )
