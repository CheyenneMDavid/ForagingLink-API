# The Foraging API

## Introduction
The **Foraging API** is a Django REST Framework Application Programming Interface for ["The Foraging Link"](), which serves as an online community, monthly foraging blog, and platform to promote seasonal foraging courses. It aims to connect people with nature and to one another whilst sharing information about the free edible delights available all around us.

## Table of Contents

- [Introduction](#introduction)
- [Table of Contents](#table-of-contents)
- [User Stories](#user-stories)
- [Applications within Project](#applications-within-project)
  - [Profiles](#profiles)
  - [Plants Blog](#plants-blog)
  - [Comments](#comments)
  - [Likes](#likes)
  - [Followers](#followers)
  - [Courses](#courses)
  - [Course Registrations](#course-registrations)
- [Planning](#planning)
  - [ERD Diagrams and Flowcharts](#erd-diagrams-and-flowcharts)
  - [Wireframes](#wireframes)
  - [Mockups](#mockups)
- [Development Choices](#development-choices)
  - [Dependency Management](#dependency-management)
- [Development Challenges & Solutions](#development-challenges--solutions)
- [Usage](#usage)
- [Agile Development Approach](#agile-development-approach)
- [Testing](#testing)
  - [Written Tests](#written-tests)
- [Future Developments](#future-developments)
- [Forking, Improving, Contributing](#forking-improving-contributing)

___

## User Stories:
The user stories utilized in this project align with those listed in the associated frontend project. This decision was made because both frontend and backend components contribute to fulfilling these user stories, albeit in different capacities. The frontend is responsible for presenting information in the user interface, while the backend manages the storage and retrieval of data. User stories for the backend were admin related and were labeled as such. But there were stories that were equally related to users and were also related accordingly.

These are a few of the admin related user stories:

- As an Admin, I want to publish blog posts so that users can read
  and engage with them through comments, increasing user interaction and participation.
  &nbsp; 
- As an Admin I have full CRUD capabilities over user accounts and
  posts by users so that I can create and manage necessary accounts to cosmetically induce social interaction, with the aim of fostering real engagement so that the social interaction between users grows more organically as the number of users increase.
  &nbsp; 
- As an Admin, I can access the registration details submitted by
  users who wish to attend foraging courses so that I can manage course registrations and communicate with participants.
  
You can find the rest of the stories [here](https://github.com/users/CheyenneMDavid/projects/38/views/1)
___

## Applications within Project
### Profiles
### Plants Blog
### Comments
### Likes
### Followers
### Courses
### Course Registrations

___

## Planning
### ERD Diagrams and Flowcharts

### Wireframes

### Mockups

___

## Development Choices
### Dependency Management

___

## Development Challenges & Solutions

- Upgraded to a newer version of Django to use `django_filter` so that the admin panel could utilise advanced filtering for the comments application. A compromise was found by using Django 4.2 and the newer version of `django_filter` 24.2, which provided the advanced filtering capabilities. However, this caused huge compatibility issues elsewhere, so I reverted to `Django==3.2.4` and `django-filter==2.4.0`.

- Compatibility issues between Python 3.12 and `django-allauth` due to depreciated features in Python 3.12 required by `django-allauth`. This was resolved via tutor guidance on Slack as it was becoming a commonly experienced issue.  The solution given was to install python version 3.9.19. This was a solution, but where I was using a virtual environment to isolate my dependencies, I found that I was having to reinstall the python version a fresh each time I started my venv.
Initially I tried to add commands for older version of python in the .bashrc file To avoid repetition of console commands. Unable to make the changes I realised that lacked the permissions required.  So instead, I created a script called `setup_venv.sh` which contained the commands I needed and allowed me to enter only one command to run it. The result was no different, but it was less commands for me.

___

## Usage

___

## Agile Development Approach

___

## Testing
### Written Tests

- **Tests for Plants Blog Application**:
  Tests to verify that only an admin user can create a PlantInFocusPost instance and that a regular user can't.
  ![Plants Blog app tests](plants_blog/tests.py)
  ![Pass Screenshot](https://res.cloudinary.com/cheymd/image/upload/v1717385041/forage/Foraging_API_README_images/plants_blog_tests_irmprb.png)
  All Tests Passed.
  &nbsp;
  &nbsp;
- **Tests for Profiles Application**:
 Tests to verify Creation, Update, and Deletion of a Profile instance given the appropriate permissions.
  ![Profiles app tests](profiles/tests.py)
  ![Pass Screenshot](https://res.cloudinary.com/cheymd/image/upload/v1717385041/forage/Foraging_API_README_images/profiles_tests_icrakl.png)
  All tests passed.
  &nbsp;
  &nbsp;
- **Tests for the Comments Application**:
  Tests to ensure that a Like instance can be created and that the same instance be associated with either a PlantInFocus instance or a Comment instance, but not both Comments and a PlantInFocus at the same time.
  ![Comments app tests](comments/tests.py)
  ![Pass Screenshot](https://res.cloudinary.com/cheymd/image/upload/v1717385041/forage/Foraging_API_README_images/comments_tests_oammrb.png)
  All tests passed.
  &nbsp;
  &nbsp;
- **Tests for the Likes Application**:
  Tests for Creation, Deletion, and Unique Constraints of a Like Instance.
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
___

## Future Developments

___

## Forking, Improving, Contributing
