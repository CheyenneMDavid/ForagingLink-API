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
  - [Models and CRUD Breakdown](#models-and-crud-breakdown)
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
The user stories utilized in this project align with those listed in the associated frontend project. This decision was made because both frontend and backend components contribute to fulfilling these user stories, albeit in different capacities. The frontend is responsible for presenting information in the user interface, so it is repeated in the corresponding repository. Whilst the backend manages the storage and retrieval of data.

| Feature       | As    | I Want To                               | So That I Can                                 | Backend Functions     
|---------------|-------|-----------------------------------------|-----------------------------------------------|-----------------------
| Authentication| user  | sign-up for an account                  | access the application securely               | `create_user()`       |
| Authentication| user  | sign in to my account securely          | use the application                           | `authenticate_user()` |
| Authentication| user  | sign out of my account securely         | ensure the privacy of my data                 | `logout_user()`       |
| Comments      | user  | edit comments                           | make corrections or updates                   | `update_comment()`    |
| Comments      | user  | delete comments                         | remove them from visibility                   | `delete_comment()`    |
| Likes         | user  | like posts and comments                 | show appreciation for content                 | `create_like()`       |
| Followers     | user  | follow other users                      | stay updated on what they have to say         | `create_follower()`   |
| Courses       | user  | register for a foraging course          | attend one                                    | `create_course_registration()`  |
| Comments      | user  | comment on posts and other comments     | interact with other users                     | `create_comment()`, `create_reply()`, `read_comments()`            |
| Posts         | admin | exercise full CRUD capability for posts | build community interest in site content      | `create_post()`, `read_posts()`, `update_post()`, `delete_post()`  |
| Courses       | admin | access user's registration details for foraging courses                                 | manage course registrations and communicate with participants      |  `retrieve_course_registrations()`|

<br>

You can find the Project with fuller details for the stories [here](https://github.com/users/CheyenneMDavid/projects/38/views/1)

___

## Applications in the Project
### Profiles
Profiles manages the user information. It provides a platform for users to create and maintain their personal accounts. This includes storing details such as usernames, emails, and profile pictures.

### Plants Blog
The purpose of this app is to create singular-format-focused posts with information that spans particular themes of interest.
To this end, only an Admin of the site can create posts, which cover useful information, themes of interest, and important warnings through appropriate images when required, whilst authenticated users can comment on them.

The Plants Blog application provides the landing page which displays an image of the plant that is the focus for the current month, followed by previous month's posts in a descending order with pagination ensuring a maximum of 10 items listed, with each item in the list being a link to it's detail page for that plant. Both lists and details can be read by all users, authenticated or not.

**The post content covers:**
- The environments in which they're found.
- Culinary uses.
- Medicinal Uses.
- Folklore.
- Information of confusable lookalikes.

### Comments
The Comments app facilitates user engagement by allowing authenticated users to comment on posts and also other user's comments. It enables enables users to engage by asking and answering questions related to the posts. Reading and creation of comments is restricted to authenticated users only.

### Likes
Likes enable users to express their appreciation for posts and comments. By liking content, they're able to show support for valuable contribution from one another. Unauthenticated users can see likes, but only authenticated users are able to add a like posts or comments

### Followers
The Followers app enables users to stay connected with content authors, including admins who create articles and users who contribute valuable comments. Only authenticated users can follow others.

### Courses
The Courses app is used to publish and manage upcoming courses in the seasons of spring, summer, and autumn. It allows all users, whether authenticated or not, to view course listings and details, while only admins have the ability to create, update, or delete courses. Each course detail page includes essential information such as the season, title, date, description, location, and maximum number of participants.

### Course Registrations
The Course Registrations app manages user registrations for the courses offered. It allows users to register for courses and stores relevant information such as contact details, dietary restrictions, and emergency contact information. The app ensures that courses are not over-subscribed by setting the registration status to "Pending" by default, which can be managed via the admin panel.
<br><br>

### Models and CRUD Breakdown
Although I have spoken about the individual applications within the project, the following table provides a quick reference allows a quicker understand the individual application's functionalities and their CRUD operations.

| Model                 | Endpoints   | Create            | Retrieve | Update | Delete | Filter          | Text Search |
|---------------------  |-------------|-------------------|----------|--------|--------|-----------------|--------------|
| PlantInFocusPost      | /plants_blog/<br>/plants_blog/:id/    | Yes(Admins only)  | Yes      | Yes    | Yes    | main_plant_name, main_plant_environment, culinary_uses, medicinal_uses, folklore, confusable_plant_name | main_plant_name, main_plant_environment, culinary_uses, medicinal_uses, folklore, confusable_plant_name |
| Comment               | /comments/<br>/comments/:id/  | Yes    | Yes      | Yes    | Yes    | plant_in_focus_post, replying_comment, owner__username | content, owner__username, plant_in_focus_post__main_plant_name |
| Like                  | /likes/<br>/likes/:id     | Yes  | Yes      | No     | Yes    | owner, plant_in_focus_post, comment    | None |
| Follower              | /followers/<br>/followers/:id | Yes         | Yes      | No     | Yes    | None  | None |
| Course                | /courses/<br>/courses/:id   | Yes    | Yes      | Yes    | Yes    | None | None  |
| CourseRegistration    | /course_registrations/<br>/course_registrations/:id                        | Yes    | Yes      | No     | Yes    | None  | None |


## Planning
### Entity-Relationship Diagrams (ERDs)
These diagrams show the structure and relationships of key components within the application that support user interaction and engagement.<br>

The **User Interaction and Authentication ERD** shows the structure of the the applications's main models and their relationships within the application. It provides an overview of the models that facilitate users to engage with one another.
![User Interaction ERD](https://res.cloudinary.com/cheymd/image/upload/v1717661021/forage/Foraging_API_README_images/user_interaction_and_authentication_erd_yll12s.png)

The **Course Management ERD** details the components involved in managing course content and user registrations submitted via contact forms. These are managed by site admins through the Django Admin Panel. This part of the application operates separately from the main user interaction features but is integrated within the same framework. It focuses on the relationships between Profiles, Courses, and Course Registrations..<br>
![Course Management ERD](https://res.cloudinary.com/cheymd/image/upload/v1717661022/forage/Foraging_API_README_images/course_management_erd_loozlc.png)

### API Structure Diagrams
These diagrams show the structure and relationships between the components in the Foraging Link API. They provide a visual representation of how users, posts, comments, likes, and followers interact within the system.

The **User Interaction and Authentication Overview** illustrates the user interaction and authentication structure within the Foraging Link API. It shows how users interact with comments, likes, blog posts, and followers, and includes the authentication component.

![User Interaction and Authentication](https://res.cloudinary.com/cheymd/image/upload/v1717661023/forage/Foraging_API_README_images/user_interaction_and_authentication_overview_u3v4sf.png)<br><br>

The **Course Management** Overview illustrates the course management structure within the Foraging Link API. It shows how users can read upcoming courses, fill out registration forms, and how admins can create and manage courses.<br>
![Course Management Overview](https://res.cloudinary.com/cheymd/image/upload/v1717788223/forage/Foraging_API_README_images/course_management_overview_nnmbfc.png)


### Wireframes

### Mockups

___
___
___
___
___
___






___
___
___
___

### Dependency Management

### Explanation of Naming Decisions
**Plants Blog App**
The name of this app could have been "Blog" for the sake of simplicity.  As could the model which I chose to call "PlantInFocusPost" rather than "Post".
Reasoning was that I wanted to convey the type and specific purpose of the blog and it's posts.
I believe the naming decisions help maintain a clear and organized codebase, making it easier for future developers to not only understand the structure, but also the purpose of the different components.

___

## Development Challenges & Solutions

- Upgraded to a newer version of Django to use `django_filter` so that the admin panel could utilize advanced filtering for the comments application. A compromise was found by using Django 4.2 and the newer version of `django_filter` 24.2, which provided the advanced filtering capabilities. However, this caused huge compatibility issues elsewhere, so I reverted to `Django==3.2.4` and `django-filter==2.4.0`.
&nbsp;
- Compatibility issues between Python 3.12 and `django-allauth` due to depreciated features in Python 3.12 required by `django-allauth`. This was resolved via tutor guidance on Slack as it was becoming a commonly experienced issue. The solution given was to install python version 3.9.19. This was a solution, but where I was using a virtual environment to isolate my dependencies, I found that I was having to reinstall the python version afresh each time I started my venv. Initially, I tried to add commands for older versions of python in the .bashrc file to avoid repetition of console commands. Unable to make the changes I realized that I lacked the permissions required. So instead, I created a script called `setup_venv.sh` which contained the commands I needed and allowed me to enter only one command to run it. The result was no different, but it was fewer commands for me.
&nbsp;
- Inconsistent Use of Hyphens and Underscores: When creating the [Models and CRUD Breakdown](#models-and-crud-breakdown) table for this readme file and adding the search and filter fields to it, I noticed that I had been inconsistent in my use of hyphens and underscores. I decided to standardize the use of underscores in all URLs and updated the `urls.py` files in each app and any corresponding file across the entire codebase. As a result, all URL patterns now use underscores.
___

___


___
___

## Use

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
