"""
This file contains tests for the Comments app.
"""

from django.test import TestCase
from django.contrib.auth.models import User
from plants_blog.models import PlantInFocusPost
from .models import Comment


class CommentModelTest(TestCase):
    """
    Tests to ensure that a comment can be created and linked to a user and a
    plant post instance.
    """

    def setUp(self):
        """
        Creates a user, a plant post, and a comment for the purpose of testing
        """

        self.user = User.objects.create_user(
            username="test_user",
            password="test_user_password",
        )

        self.post = PlantInFocusPost.objects.create(
            main_plant_name="Test Plant", owner=self.user
        )

        self.comment = Comment.objects.create(
            owner=self.user,
            plant_in_focus_post=self.post,
            content="Test comment",
        )

    def test_comment_creation(self):
        """
        Test logic to check that a comment has been created.
        Initially checking the attributes of the comment, it verifies that
        the content, owner, and plant post are correctly associated with the
        comment.
        """

        self.assertEqual(self.comment.content, "Test comment")
        self.assertEqual(self.comment.owner, self.user)
        self.assertEqual(self.comment.plant_in_focus_post, self.post)

    def test_comment_str(self):
        """
        Tests the string representation of the comment.
        Verifies that the __str__ method of the comment model returns the
        comment content.
        """
        self.assertEqual(str(self.comment), "Test comment")

    def test_third_level_comment_restriction(self):
        """
        Tests to ensure that comments can't go passed 2 levels
        """

        second_level_reply = Comment.objects.create(
            owner=self.user,
            plant_in_focus_post=self.post,
            replying_comment=self.comment,
            content="Second level reply",
        )

        with self.assertRaises(ValueError):
            # Expecting a ValueError when trying to create a third-level
            # reply, which should be disallowed by model validation.
            # The variable 'third_level_comment' is used only for this purpose
            # and shows as an error because it appears not to be used.
            third_level_reply = Comment.objects.create(
                owner=self.user,
                plant_in_focus_post=self.post,
                replying_comment=second_level_reply,
                content="Third level reply",
            )
