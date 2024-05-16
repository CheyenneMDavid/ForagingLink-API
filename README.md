# Foraging Link API

Apps in Project:

Profiles.
Plants Blog.
Comments

## Development Choices
### Dependency Management:
Upgraded to a newer version of Django in order to use django_filter so that the admin panel could utilize advanced filtering for the comments application.
A compromise was found by using Django 4.2 and the older version of django_filter 24.2 which provided the advanced filtering capabilities.
The compromise of versions allowed the latest features and improvements whilst ensuring compatibility across dependencies.
Whilst `CSRF_TRUSTED_ORIGINS = ["https://*.gitpod.io"]` was added to the settings.py as a temporary fix during development.
___
## Tests

### Written Tests

- **Tests for Plants Blog Application**:
  Tests to verify that only an admin user can create a PlantInFocusPost instance and that a regular user can't.
  ![Plants Blog app tests](plants_blog/tests.py)
  ![Pass Screenshot](https://res.cloudinary.com/cheymd/image/upload/v1715867067/forage/Foraging_API_README_images/plants-blog-test-results_vxfyy9.png)
  All Tests Passed.
  &nbsp;
  &nbsp;
  
- **Tests for Profiles Application**:
 Tests to verify Creation, Update and Deletion of a Profile instance
  given the appropriate permissions.
  ![Profiles app tests](profiles/tests.py)
  ![Pass Screenshot](https://res.cloudinary.com/cheymd/image/upload/v1715502789/forage/Foraging_API_README_images/api_profile_test_results_vitisr.png)
  All tests passed.
  &nbsp;
  &nbsp;
- **Tests for the Comments Application**:
  Tests to ensure that a Like instance can be created and that same instance be associated with either a PlantInFocus instance or a Comment instance, but not both Comments and a PlantInFocus at the same time.
  ![Comments app tests](comments/tests.py)
  ![Pass Screenshot](https://res.cloudinary.com/cheymd/image/upload/v1715868706/forage/Foraging_API_README_images/comments-test-results_rwwqxh.png)
  All tests passed.
  &nbsp;
  &nbsp;
- Tests for Creation, Deletion and Unique Constraints of a Like Instance
  ![Tests for Likes App.](likes/tests.py)
  ![Tests Pass](https://res.cloudinary.com/cheymd/image/upload/v1715869305/forage/Foraging_API_README_images/likes-test-results_rxw4eb.png)
  All tests passed.