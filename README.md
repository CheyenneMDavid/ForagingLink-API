# Foraging Link API

Apps in Project:

Profiles.
Plants Blog.
Comments

## Development Choices
### Dependency Management:


___
## Development Challenges & Solutions.

- Upgraded to a newer version of Django in order to use django_filter so that the admin panel could utilize advanced filtering for the comments application.
A compromise was found by using Django 4.2 and the newer version of django_filter 24.2 which provided the advanced filtering capabilities.  But this caused huge compatibility issues so finally reverted to `Django==3.2.4` and `django-filter==2.4.0`, allowing me to remove the `CSRF_TRUSTED_ORIGINS = ["https://*.gitpod.io"]` from `settings.py`.

- Compatibility issues between Python 3.12 and `django-allauth` due to depreciated features in Python 3.12 which were required by `django-allauth`.  This was resolved via tutor guidance on slack as it was becoming a commonly experienced issue.
___
## Tests

### Written Tests

- **Tests for Plants Blog Application**:
  Tests to verify that only an admin user can create a PlantInFocusPost instance and that a regular user can't.
  ![Plants Blog app tests](plants_blog/tests.py)
  ![Pass Screenshot](https://res.cloudinary.com/cheymd/image/upload/v1717385041/forage/Foraging_API_README_images/plants_blog_tests_irmprb.png)
  All Tests Passed.
  &nbsp;
  &nbsp;
  
- **Tests for Profiles Application**:
 Tests to verify Creation, Update and Deletion of a Profile instance
  given the appropriate permissions.
  ![Profiles app tests](profiles/tests.py)
  ![Pass Screenshot](https://res.cloudinary.com/cheymd/image/upload/v1717385041/forage/Foraging_API_README_images/profiles_tests_icrakl.png)
  All tests passed.
  &nbsp;
  &nbsp;
- **Tests for the Comments Application**:
  Tests to ensure that a Like instance can be created and that same instance be associated with either a PlantInFocus instance or a Comment instance, but not both Comments and a PlantInFocus at the same time.
  ![Comments app tests](comments/tests.py)
  ![Pass Screenshot](https://res.cloudinary.com/cheymd/image/upload/v1717385041/forage/Foraging_API_README_images/comments_tests_oammrb.png)
  All tests passed.
  &nbsp;
  &nbsp;
- **Tests for the Likes Application**:
  Tests for Creation, Deletion and Unique Constraints of a Like Instance
  ![Likes app tests](likes/tests.py)
  ![Pass Screenshot](https://res.cloudinary.com/cheymd/image/upload/v1717385041/forage/Foraging_API_README_images/likes_tests_lypugq.png)
  All tests passed.
  &nbsp;
  &nbsp;
- **Tests for Courses App**:
  Tests to validate the functionality of the Course API views, including listing, creating, updating, and deleting courses, ensuring proper HTTP status codes are returned.
  ![Courses app tests](courses/tests.py)
  ![Pass Screenshot](https://res.cloudinary.com/cheymd/image/upload/v1717385041/forage/Foraging_API_README_images/courses_tests_tnodju.png)
  All tests passed.
  &nbsp;
  &nbsp;
- **Tests for Course Registrations App**:
  Tests to verify that a CourseRegistration instance can be created with all the necessary fields populated and that the default status of "Pending" is applied to new instances.
  ![Course Registrations app tests](course_registrations/tests.py)
  ![Pass Screenshot](https://res.cloudinary.com/cheymd/image/upload/v1717385040/forage/Foraging_API_README_images/course_registrations_uq9m5h.png)
  All tests passed.
  
  