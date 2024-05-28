from django.test import TestCase
from django.contrib.auth.models import User
from courses.models import Course
from course_registrations.models import CourseRegistration
from datetime import date


class CourseRegistrationModelTest(TestCase):
    """
    Tests for the CourseRegistration model
    """

    def setUp(self):
        """
        Sets up the data to be used in the tests.
        """
        self.user = User.objects.create_user(
            username="test_user", password="test_password"
        )
        self.course = Course.objects.create(
            title="Test Course",
            date=date.today(),
            description="Test Description",
            location="Test Location",
        )

    def test_create_course_registration(self):
        """
        Tests that a course registration instance can be created.
        """
        registration = CourseRegistration.objects.create(
            course_title=self.course,
            owner=self.user,
            email="testuser@example.com",
            phone="1234567890",
            ice_name="Emergency Contact",
            ice_number="0987654321",
            dietary_restrictions="None",
            is_driver=True,
        )
        self.assertEqual(registration.owner.username, "test_user")
        self.assertEqual(registration.course_title.title, "Test Course")
        self.assertEqual(registration.email, "testuser@example.com")
        self.assertEqual(registration.phone, "1234567890")
        self.assertEqual(registration.ice_name, "Emergency Contact")
        self.assertEqual(registration.ice_number, "0987654321")
        self.assertEqual(registration.dietary_restrictions, "None")
        self.assertTrue(registration.is_driver)

    def test_default_status(self):
        """
        Tests that the default status of "Pending" is applied to a new
        instance when it's created.
        """
        registration = CourseRegistration.objects.create(
            course_title=self.course,
            owner=self.user,
            email="testuser@example.com",
            phone="1234567890",
            ice_name="Emergency Contact",
            ice_number="0987654321",
        )
        self.assertEqual(registration.status, "Pending")
