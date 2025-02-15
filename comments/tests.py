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
            main_plant_name="Test Plant",
            main_plant_month="1",
            main_plant_environment="Forest",
            culinary_uses="Edible leaves",
            history_and_folklore="Used in traditional medicine",
            main_plant_parts_used="Leaves and stems",
            owner=self.user,
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
            Comment.objects.create(
                owner=self.user,
                plant_in_focus_post=self.post,
                replying_comment=second_level_reply,
                content="Third level reply",
            )

        # Confirms that there is no third-level comment was saved.
        # Checks to see the number of comments replying to the
        # 'second_level_reply' is 0, thereby ensuring that no third-level
        # comments were saved in the database.
        self.assertEqual(
            Comment.objects.filter(
                replying_comment=second_level_reply
            ).count(),
            0,
        )
