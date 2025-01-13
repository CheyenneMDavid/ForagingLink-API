from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Course


class CourseAPITest(TestCase):
    """
    Tests for the Course API views.
    This includes setting up the data needed for the test environment:
    a test client, an admin user, and a sample course with data for the fields.
    It then tests the listing, creating, updating, and deleting of courses,
    ensuring the correct HTTP status codes are returned.
    """

    def setUp(self):
        """
        Sets up the test environment.
        Creates a test client, an admin user, and a sample course for testing.
        """
        self.client = APIClient()
        self.admin_user = User.objects.create_superuser(
            username="admin",
            password="password",
        )
        self.client.login(username="admin", password="password")
        self.course = Course.objects.create(
            season="Spring",
            title="Test Course",
            date="2028-06-01",
            description="Test Course Description",
            location="Test Course Location",
            max_capacity=10,
        )

    def test_course_list(self):
        """
        Tests the CourseList view to ensure it returns a list of courses
        with an HTTP 200 OK status.

        The test asserts that the response contains at least one course.
        If the response is empty, the test fails with "Response data is empty."
        """
        response = self.client.get("/courses/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(
            len(response.data["results"]),
            0,
            "Response data is empty",
        )
        if len(response.data["results"]) > 0:
            self.assertEqual(
                response.data["results"][0]["title"],
                self.course.title,
            )

    def test_valid_course_creation(self):
        """
        Tests the CourseCreate view with valid data to ensure a new course can
        be created and returns an HTTP 201 CREATED status.
        """
        valid_course_data = {
            "season": "Summer",
            "title": "Valid Test Course",
            "date": "2024-07-01",
            "description": "Valid Test Course Description",
            "location": "Valid Test Location",
            "max_capacity": 10,
        }
        response = self.client.post("/courses/create/", valid_course_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_course_creation(self):
        """
        Tests the CourseCreate view with invalid data to ensure a course
        cannot be created with max_capacity exceeding 10, resulting in an
        HTTP 400 BAD REQUEST response.

        Note: This test intentionally triggers a "Bad Request" log due to
        the invalid data.
        """
        invalid_course_data = {
            "season": "Summer",
            "title": "Invalid Test Course",
            "date": "2024-07-01",
            "description": "Invalid Test Course Description",
            "location": "Invalid Test Location",
            "max_capacity": 12,
        }
        response = self.client.post("/courses/create/", invalid_course_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_course_update(self):
        """
        Tests the CourseUpdateDelete view with valid data to ensure a course
        can be updated and returns an HTTP 200 OK status.
        """
        valid_update_data = {
            "season": "Summer",
            "title": "Updated Valid Course",
            "date": "2024-08-02",
            "description": "Updated Valid Description",
            "location": "Updated Valid Location",
            "max_capacity": 8,
        }
        response = self.client.put(
            f"/courses/{self.course.id}/",
            valid_update_data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_course_update_invalid(self):
        """
        Tests the CourseUpdateDelete view with invalid data to ensure a course
        cannot be updated with max_capacity exceeding 10, resulting in an
        HTTP 400 BAD REQUEST response.

        Note: This test intentionally triggers a "Bad Request" log due to
        the invalid data.
        """
        invalid_update_data = {
            "season": "Summer",
            "title": "Updated Invalid Course",
            "date": "2024-08-02",
            "description": "Updated Invalid Description",
            "location": "Updated Invalid Location",
            "max_capacity": 20,
        }
        response = self.client.put(
            f"/courses/{self.course.id}/",
            invalid_update_data,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_course_delete(self):
        """
        Tests the CourseUpdateDelete view to ensure a course can be deleted,
        returning an HTTP 204 NO CONTENT status, confirming the course is
        removed.
        """
        response = self.client.delete(f"/courses/{self.course.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.count(), 0)
