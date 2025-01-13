# The tests for Course Registrations expect the status of a registration
# to default to "Confirmed".
# Upon registration, if spaces are available on a
# course, they are dynamically calculated and updated to reflect the remaining
# availability.


from django.test import TestCase
from django.contrib.auth.models import User
from courses.models import Course
from course_registrations.models import CourseRegistration
from datetime import date
from phonenumbers import parse


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
        Tests that a course registration instance can be created, ensuring
        that they are tested with valid phone numbers for both mobile and
        landlines.
        """
        registration = CourseRegistration.objects.create(
            course_title=self.course,
            owner=self.user,
            email="testuser@example.com",
            phone="+447885144123",
            ice_name="Emergency Contact",
            ice_number="+447885422133",
            dietary_restrictions="None",
            is_driver=True,
        )

        # Using the "parse()" function to convert the phone number strings
        # into PhoneNumber objects so they're compared properly.
        # Ensuring both the expected and actual phone numbers
        # are in the same format, also incorporating the country code for
        # validation
        expected_phone = parse("+447885144123", "GB")
        expected_ice_number = parse("+447885422133", "GB")

        self.assertEqual(registration.owner.username, "test_user")
        self.assertEqual(registration.course_title.title, "Test Course")
        self.assertEqual(registration.email, "testuser@example.com")
        self.assertEqual(registration.phone, expected_phone)
        self.assertEqual(registration.ice_name, "Emergency Contact")
        self.assertEqual(registration.ice_number, expected_ice_number)
        self.assertEqual(registration.dietary_restrictions, "None")
        self.assertTrue(registration.is_driver)

    def test_default_status(self):
        """
        Tests that the default status of "Confirmed" is applied to a new
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
        self.assertEqual(registration.status, "Confirmed")
