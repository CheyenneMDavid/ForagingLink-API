from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Course


class CourseAPITest(TestCase):
    """
    Tests for the Course API views.
    This includes setting up all the data that is needed for the test
    environment. A test client, an admin user, and a sample course with  data
    for the fields.
    It then tests the listing, creating, updating, and the deleting of courses
    and returns the relevant http status codes.
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
        Tests the CourseList view to ensure it can return a list of courses
        and returns a HTTP status of 200 OK.

        The test asserts that the response contains at least one course.
        If the response is empty, "Response data is empty" is printed in the
        test output and the test fails. If the response contains courses, the
        title of the first course in the response is compared to the title of
        the course created in the setup method.
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
        be created and returns a http status of 201 as confirmation, it's
        done.
        """
        # Data for testing a valid course creation.
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
        Tests the CourseCreate view with invalid data to ensure that a course
        can NOT be created with max_capacity EXCEEDING 10 and returns a http
        code of 400 BAD REQUEST.
        """
        # Data for testing a INVALID course creation. Namely, the max_capacity
        # figure of 12 that exceeds the 10, allowed.
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
        Tests the CourseUpdateDelete view with valid data to ensure that a
        course can be updated and returns a http status code of 200 OK to show
        success.
        """
        # Data for testing a valid course update.
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
        Test the CourseUpdateDelete view with invalid data to ensure a course
        can't be updated with max_capacity exceeding 10.
        """
        # Data for testing a INVALID course update. Namely, the max_capacity
        # figure of 20 that exceeds the 10, allowed.
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
        Test the CourseUpdateDelete view to ensure a course can be deleted and
        returns a http status of 204 confirming that the content is no longer
        there.
        """
        response = self.client.delete(f"/courses/{self.course.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.count(), 0)
