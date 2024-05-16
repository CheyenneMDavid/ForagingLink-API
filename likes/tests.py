"""
Tests for the Like model.
They ensure that the basic functions of creation, deletion, and the unique
constraints function as intended.
"""

from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from likes.models import Like
from plants_blog.models import PlantInFocusPost
from comments.models import Comment


class LikeModelTest(APITestCase):
    """
    Tests the basic functionality of the Like model, including creation,
    deletion, and unique constraints.
    """

    def setUp(self):
        """
        Sets up the test environment by creating a test user, a test plant
        post, and a test comment for use.
        """
        self.user = User.objects.create_user(
            username="test_user", password="test_password"
        )
        self.post = PlantInFocusPost.objects.create(
            main_plant_name="Test Plant",
        )
        self.comment = Comment.objects.create(
            content="Test Comment", plant_in_focus_post=self.post
        )

    def test_like_creation_for_post(self):
        """
        Tests that a like instance can be created for a PlantInFocusPost.
        """
        like = Like.objects.create(
            owner=self.user,
            plant_in_focus_post=self.post,
        )
        self.assertEqual(Like.objects.count(), 1)

    def test_like_creation_for_comment(self):
        """
        Tests that a like instance can be created for a Comment.
        """
        like = Like.objects.create(owner=self.user, comment=self.comment)
        self.assertEqual(Like.objects.count(), 1)

    def test_unique_constraint_for_post(self):
        """
        Tests that a user can't like the same PlantInFocusPost more than once.
        """
        Like.objects.create(owner=self.user, plant_in_focus_post=self.post)
        with self.assertRaises(Exception):
            Like.objects.create(owner=self.user, plant_in_focus_post=self.post)

    def test_unique_constraint_for_comment(self):
        """
        Tests that a user can't like the same Comment more than once.
        """
        Like.objects.create(owner=self.user, comment=self.comment)
        with self.assertRaises(Exception):
            Like.objects.create(owner=self.user, comment=self.comment)

    def test_like_deletion(self):
        """
        Tests that a like instance can be deleted.
        """
        like = Like.objects.create(
            owner=self.user,
            plant_in_focus_post=self.post,
        )
        like.delete()
        self.assertEqual(Like.objects.count(), 0)
