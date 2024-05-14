# Foraging Link API

Apps in Project:

Profiles.
Plants Blog.
Comments

## Development Choices
### Dependency Management:
Upgraded to a newer version of Django in order to use django_filter so that the admin panel could utilize advanced filtering for the comments application.  Experienced compatibility issues when using Django 5.0 which played havoc with the CSRF settings.
A compromise was found by using Django 4.2 and the older version of django_filter 24.2 which provided the advanced filtering capabilities.
The compromise of versions allowed the latest features and improvements whilst ensuring compatibility across dependencies.
___
## Tests

### Written Tests
- Tests for Plants Blog Application:
  Tests to verify that only an admin user can create a post `plant_in_focus_post` and that a regular user can't.
  ![Tests for creating posts for the blog](plants_blog/tests.py)
  ![Test Pass](https://res.cloudinary.com/cheymd/image/upload/v1715320492/forage/Foraging_API_README_images/api_blog_post_test_results_in3np5.png)
  All Tests Passed.
  &nbsp;
  &nbsp;
- Tests for the Profiles Application:
  ![Testing of Creating, Updating and Deleting Profiles](profiles/tests.py)
  ![Tests Pass](https://res.cloudinary.com/cheymd/image/upload/v1715502789/forage/Foraging_API_README_images/api_profile_test_results_vitisr.png)
  All tests passed.