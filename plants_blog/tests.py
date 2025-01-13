"""
This file has been written through guidance gained from the DRF-API
walkthrough project with Code Institute and documentation from:
https://www.django-rest-framework.org

The file contains test cases for the PlantInFocusPostListView class.
It verifies that only an admin user can create a post, whilst a normal
authenticated user is restricted from creating post.
For more information on writing tests using Django Rest Framework, refer to:
https://www.django-rest-framework.org/api-guide/testing/
"""

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase


class PlantInFocusPostListViewTests(APITestCase):
    """
    Test to ensure that only an admin_user can create a post.
    """

    def setUp(self):
        """
        Creates an instance of the APIClient.
        Creates an admin_user and a regular_user for their respective
        abilities to create or not create posts, according to permissions.
        """

        self.admin_user = User.objects.create_superuser(
            username="admin_user",
            password="admin_password",
        )
        self.normal_user = User.objects.create_user(
            username="regular_user",
            password="user_password",
        )

    def test_logged_in_admin_can_create_post(self):
        """
        Checks that an admin user can create a post successfully by simulating
        authentication as an admin user and making a POST request to create a
        post.
        Verifies successful creation of post by returning a status of:
        HTTP_201_CREATED
        """
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.post(
            "/plants_blog/posts/create/",
            # Data for creating a test post
            data={
                "main_plant_name": "Dandelion",
                "main_plant_month": 5,
                "main_plant_environment": "Meadows and fields",
                "culinary_uses": "Can be used in salads and teas",
                "history_and_folklore": "Symbol of resilience in folklore",
                "main_plant_parts_used": "Leaves, roots, flowers",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_normal_user_cannot_create_post(self):
        """
        Checks that a normal user can't create a post by simulating
        authentication as a normal user and making a POST request to create a
        post.
        Verifies that the regular/normal authenticated user can't create a
        post by returning a status of: HTTP_403_FORBIDDEN
        """
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.post(
            "/plants_blog/posts/create/",
            # Data for creating a test post.
            data={
                "main_plant_name": "Dandelion",
                "main_plant_month": 5,
                "main_plant_environment": "Meadows and fields",
                "culinary_uses": "Can be used in salads and teas",
                "history_and_folklore": "Named 'Wet your bed' by children",
                "main_plant_parts_used": "Leaves, roots, flowers",
            },
        )
        print("Response Status Code:", response.status_code)
        print("Response Content:", response.content)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
