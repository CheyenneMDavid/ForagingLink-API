# The Foraging API

## Project description

The **Foraging API** is a Django REST Framework Application Programming Interface for ["The Foraging Link"](), which serves as an online community, monthly foraging blog, and platform to promote seasonal foraging courses. It aims to connect people with nature and to one another whilst sharing information about the free edible delights available all around us.

## Table of Contents

- [The Foraging API](#the-foraging-api)
  - [Project description](#project-description)
  - [Table of Contents](#table-of-contents)
  - [User Stories:](#user-stories)
  - [Applications in the Project](#applications-in-the-project)
    - [Profiles](#profiles)
    - [Plants Blog](#plants-blog)
      - [Content of Individual Blog Post](#content-of-individual-blog-post)
    - [Comments](#comments)
    - [Likes](#likes)
    - [Followers](#followers)
    - [Courses](#courses)
    - [Course Registrations](#course-registrations)
    - [Models and CRUD Breakdown](#models-and-crud-breakdown)
  - [Planning](#planning)
    - [Entity-Relationship Diagrams (ERDs)](#entity-relationship-diagrams-erds)
    - [User Interaction and Authentication ERD](#user-interaction-and-authentication-erd)
    - [Course Management ERD](#course-management-erd)
    - [API Structure Diagrams](#api-structure-diagrams)
    - [User Interaction and Authentication Overview](#user-interaction-and-authentication-overview)
    - [Course Management](#course-management)
    - [Wireframes and Mockups](#wireframes-and-mockups)
  - [Explanation of Naming Decisions](#explanation-of-naming-decisions)
  - [Development Challenges \& Solutions](#development-challenges--solutions)
    - [Version Conflicts](#version-conflicts)
    - [Naming Conventions](#naming-conventions)
    - [Pagination Conflict in Courses App](#pagination-conflict-in-courses-app)
  - [Prerequisites](#prerequisites)
  - [Dependency Management](#dependency-management)
  - [Deployment Instructions](#deployment-instructions)
    - [Note on ElephantSQL Service](#note-on-elephantsql-service)
  - [Agile Development Approach](#agile-development-approach)
    - [Key Practices](#key-practices)
    - [Examples of Agile Practices in Backend Development](#examples-of-agile-practices-in-backend-development)
    - [Example Project Boards](#example-project-boards)
  - [Testing](#testing)
    - [Written Tests](#written-tests)
  - [Future Developments](#future-developments)
  - [Forking, Improving, Contributing](#forking-improving-contributing)
    - [Making Your Changes](#making-your-changes)
    - [Submit Pull Request](#submit-pull-request)
  - [Credits](#credits)

---

## User Stories:

The user stories utilized in this project align with those listed in the associated frontend project. This decision was made because both frontend and backend components contribute to fulfilling these user stories, albeit in different capacities. The frontend is responsible for presenting information in the user interface, so it is repeated in the corresponding repository. Whilst the backend manages the storage and retrieval of data.

| Feature              | As    | I Want To                                | So That I Can                                 | Backend Functions                                                  |
| -------------------- | ----- | ---------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------ |
| Authentication       | user  | sign-up for an account                   | access the application securely               | Managed by Django Allauth                                          |
| Authentication       | user  | sign in to my account securely           | use the application                           | Managed by Django Allauth                                          |
| Authentication       | user  | sign out of my account securely          | ensure the privacy of my data                 | Managed by Django Allauth                                          |
| Comments             | user  | read comments and replies                | engage with discussions                       | `list()`, `retrieve()` (via `CommentList()`, `CommentDetail()`     |
| Comments             | user  | create comments or replies               | ask or answer questions on posts or comments  | `create()` via `CommentLis()`                                      |
| Comments             | user  | edit comments                            | make corrections or updates                   | `update()` via `CommentDetail()`                                   |
| Comments             | user  | delete comments                          | remove my comments from the post              | `destroy()` via `CommentDetail()`                                  |
| Likes                | user  | like a post or comment                   | show appreciation for what's been written     | `create()` via `LikeList()`                                        |
| Likes                | user  | unlike a post or comment                 | unlike if I changed my mind                   | `destroy()` via `LikeDetail()`                                     |
| Followers            | user  | follow other users                       | I can engage with content that interests me.  | `create()` via `FollowerList()`                                    |
| Followers            | user  | unfollow other users                     | disengage from content that I no longer enjoy | `destroy()` via `FollowerDetail()`                                 |
| Courses              | user  | view avaliable courses.                  | choose one I wish to go on.                   | `list()` via `CourseList()`, `retrieve()` via `CourseUpdateDelete` |
| Courses              | admin | create courses                           | plan and publish future events                | `CourseCreate()`                                                   |
| Courses              | admin | Update and Delete                        | update course details and remove old courses  | `update()`, `destroy()` via `CourseUpdateDelete()`                 |
| Course Registrations | user  | fill out a contact form                  | register my interest in attending a course    | `CourseRegistrationCreate()`                                       |
| Course Registrations | admin | have full CRUD ability for contact forms | manage course attendees.                      | `CourseRegistrationDetail()`                                       |
| Plant Blog           | admin | have full CRUD capability for posts      | Manage site content                           | `PlantInFocusPostCreate()`                                         |
| Plants Blog          | user  | read blog posts                          | learn about the plants I wish to foarage      | `PlantInFocusPostList()`                                           |
| Profiles             | user  | read user's profiles details             | engage with my fellow users                   | `list()` via `ProfileList()`, `retrieve()` via `ProfileDetail()`   |
| Profiles             | owner | update and delete my profile             | update my info or delete my account           | `ProfileDetail()`                                                  |

<br>

You can find the Project with fuller details for the stories [here](https://github.com/users/CheyenneMDavid/projects/38/views/1)

---

## Applications in the Project

### Profiles

Profiles manages the user information. It provides a platform for users to create and maintain their personal accounts. This includes storing details such as usernames, emails, and profile pictures.

### Plants Blog

The purpose of this app is to create singular-format-focused posts with information that spans particular themes of interest.
To this end, only an Admin of the site can create posts, which cover useful information, themes of interest, and important warnings through appropriate images when required, whilst authenticated users can comment on them.

The Plants Blog application provides the landing page which displays an image of the plant that is the focus for the current month, followed by previous month's posts in a descending order with pagination ensuring a maximum of 10 items listed, with each item in the list being a link to it's detail page for that plant. Both lists and details can be read by all users, authenticated or not.

#### Content of Individual Blog Post

- The environments in which they're found.
- Culinary uses.
- Medicinal Uses.
- Folklore.
- Information of confusable lookalikes.

### Comments

The Comments app facilitates user engagement by allowing authenticated users to comment on posts and also other user's comments. It enables enables users to engage by asking and answering questions related to the posts. Reading and creation of comments is restricted to authenticated users only and also restricted to to two levels deep so that comments are easier to manage.

### Likes

Likes enable users to express their appreciation for posts and comments. By liking content, they're able to show support for valuable contribution from one another. Unauthenticated users can see likes, but only authenticated users are able to add a like posts or comments

### Followers

The Followers app enables users to stay connected with content authors, including admins who create articles and users who contribute valuable comments. Only authenticated users can follow others.

### Courses

The Courses app is used to publish and manage upcoming courses in the seasons of spring, summer, and autumn. It allows all users, whether authenticated or not, to view course listings and details, while only admins have the ability to create, update, or delete courses. Each course detail page includes essential information such as the season, title, date, description, location, and maximum number of participants.

### Course Registrations

The Course Registrations app manages user registrations for the courses offered. It allows users to register for courses and stores relevant information such as contact details, dietary restrictions, and emergency contact information. The app ensures that courses are not over-subscribed by setting the registration status to "Pending" by default, which can be managed via the admin panel.

### Models and CRUD Breakdown

Although I have spoken about the individual applications within the project, the following table provides a quick reference allows a quicker understand the individual application's functionalities and their CRUD operations.

| Model              | Endpoints                                           | Create           | Retrieve | Update | Delete | Filter                                                                                                  | Text Search                                                                                             |
| ------------------ | --------------------------------------------------- | ---------------- | -------- | ------ | ------ | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| PlantInFocusPost   | /plants_blog/<br>/plants_blog/:id/                  | Yes(Admins only) | Yes      | Yes    | Yes    | main_plant_name, main_plant_environment, culinary_uses, medicinal_uses, folklore, confusable_plant_name | main_plant_name, main_plant_environment, culinary_uses, medicinal_uses, folklore, confusable_plant_name |
| Comment            | /comments/<br>/comments/:id/                        | Yes              | Yes      | Yes    | Yes    | plant_in_focus_post, replying_comment, owner\_\_username                                                | content, owner**username, plant_in_focus_post**main_plant_name                                          |
| Like               | /likes/<br>/likes/:id                               | Yes              | Yes      | No     | Yes    | owner, plant_in_focus_post, comment                                                                     | None                                                                                                    |
| Follower           | /followers/<br>/followers/:id                       | Yes              | Yes      | No     | Yes    | None                                                                                                    | None                                                                                                    |
| Course             | /courses/<br>/courses/:id                           | Yes              | Yes      | Yes    | Yes    | None                                                                                                    | None                                                                                                    |
| CourseRegistration | /course_registrations/<br>/course_registrations/:id | Yes              | Yes      | No     | Yes    | None                                                                                                    | None                                                                                                    |

## Planning

### Entity-Relationship Diagrams (ERDs)

These diagrams show the structure and relationships of key components within the application that support user interaction and engagement.

### User Interaction and Authentication ERD

This shows the structure of the the applications's main models and their relationships within the application. It provides an overview of the models that facilitate users to engage with one another.
![User Interaction ERD](https://res.cloudinary.com/cheymd/image/upload/v1717661021/forage/Foraging_API_README_images/user_interaction_and_authentication_erd_yll12s.png)

### Course Management ERD

This details the components involved in managing course content and user registrations submitted via contact forms. These are managed by site admins through the Django Admin Panel. This part of the application operates separately from the main user interaction features but is integrated within the same framework. It focuses on the relationships between Profiles, Courses, and Course Registrations.
![Course Management ERD](https://res.cloudinary.com/cheymd/image/upload/v1717661022/forage/Foraging_API_README_images/course_management_erd_loozlc.png)

### API Structure Diagrams

These diagrams show the structure and relationships between the components in the Foraging Link API. They provide a visual representation of how users, posts, comments, likes, and followers interact within the system.

### User Interaction and Authentication Overview

This illustrates the user interaction and authentication structure within the Foraging Link API. It shows how users interact with comments, likes, blog posts, and followers, and includes the authentication component.
![User Interaction and Authentication](https://res.cloudinary.com/cheymd/image/upload/v1717661023/forage/Foraging_API_README_images/user_interaction_and_authentication_overview_u3v4sf.png)

### Course Management

This Overview illustrates the course management structure within the Foraging Link API. It shows how users can read upcoming courses, fill out registration forms, and how admins can create and manage courses.
![Course Management Overview](https://res.cloudinary.com/cheymd/image/upload/v1717788223/forage/Foraging_API_README_images/course_management_overview_nnmbfc.png)

### Wireframes and Mockups

Wireframes and Mockups can be found in a separate repository which handles the React based User Interface [here](https://github.com/CheyenneMDavid/foraging-link-ui)

---

## Explanation of Naming Decisions

**Plants Blog App**
The name of this app could have been "Blog" for the sake of simplicity. As could the model which I chose to call "PlantInFocusPost" rather than "Post".
Reasoning was that I wanted to convey the type and specific purpose of the blog and it's posts.
I believe the naming decisions help maintain a clear and organized codebase, making it easier for future developers to not only understand the structure, but also the purpose of the different components.

---

## Development Process

### Refining the User Story Table

When going through the README.md, , I noticed some gaps in my understanding of how:

- The projects repository's User Stories.
- The written explanation of what was needed to achieve them.
- The names of the Classes, Functions, and Methods all tied together and were called upon to achieve them.

Add to this the differentiation between Classes and Functions which are designated by starting with `def`, but when writing Classes with blocks of code within them, the subordinate blocks of code, still starting with `def` were now called methods.

When writing the table describing User Stories, I had made more of a generalised statement which was kind of woolly, indicating that the individual stories would be fulfilled by tasks that would be undertaken, adding a parenthesis to them to indicate that they'd be carried out by functions within the code.

Realising the inaccuracy of my generalised back-end descriptions, I've since gone back through the table, breaking down it's content into a more structured form and associated the back-end functions, using their fuller and more precise names.

## Development Challenges & Solutions

### Version Conflicts

- Upgraded to a newer version of Django to use `django_filter` so that the admin panel could utilize advanced filtering for the comments application. A compromise was found by using Django 4.2 and the newer version of `django_filter` 24.2, which provided the advanced filtering capabilities. However, this caused huge compatibility issues elsewhere, so I reverted to `Django==3.2.4` and `django-filter==2.4.0`.

- Compatibility issues between Python 3.12 and `django-allauth` due to depreciated features in Python 3.12 required by `django-allauth`. This was resolved via tutor guidance on Slack as it was becoming a commonly experienced issue. The solution given was to install python version 3.9.19. This was a solution, but where I was using a virtual environment to isolate my dependencies, I found that I was having to reinstall the python version afresh each time I started my venv. Initially, I tried to add commands for older versions of python in the .bashrc file to avoid repetition of console commands. Unable to make the changes I realized that I lacked the permissions required. So instead, I created a script called `setup.sh`, hoping that this would allow me to enter a single command of: `./setup.sh`, but unfortunately, I couldn't seem to get it to create, start the virtual environment and load the requirements.txt as I needed, so I eventually resorted to entering the commands manually, again.

### Naming Conventions

- Inconsistent Use of Hyphens and Underscores: When creating the [Models and CRUD Breakdown](#models-and-crud-breakdown) table for this readme file and adding the search and filter fields to it, I noticed that I had been inconsistent in my use of hyphens and underscores. I decided to standardize the use of underscores in all URLs and updated the `urls.py` files in each app and any corresponding file across the entire codebase. As a result, all URL patterns now use underscores.

### Pagination Conflict in Courses App

- When initially writing the tests for the Courses app, all tests passed. However, during final testing, they started to fail. I traced the issue back to the implementation of global pagination settings in the main app's `settings.py` which I had copied from the DRF-API walkthrough project with Code Institute, because it was a good fit with the page structures. Specifically, these lines:<br>`"DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
"PAGE_SIZE": 10,`
  However, these settings applied pagination structure to all list views, including the CourseList view. This changed the response data structure, placing the results within a results key and expecting 10 items per page due to this being globally set.<br>
  This conflicted with the Courses app tests, which expected a simpler list of courses. The tests failed because they didn't account for the results key in the paginated response.
  For a detailed explanation of the solution, please refer to the [Testing](#testing) section and scroll to "Tests for courses app".

### Limiting Comment Nesting

- It was only when I was creating wireframes for the front end that I realized I had not placed a limit on the comments. As things stood, the nesting could have gotten out of hand. To guard against this, I added a restriction that limits comments to two levels, along with a test with the raising of a `ValueError` if a user attempts to create a third-level comment.

---

## Prerequisites

- Python 3.9.19
- Django 3.2.4
- Django REST Framework 3.15.1
- Cloudinary 1.40.0
- PostgreSQL database

---

## Dependency Management

**Ensure the following key libraries are installed:**

- `Django==3.2.4`
- `djangorestframework==3.15.1`
- `dj-rest-auth==2.1.9`
- `djangorestframework-simplejwt==4.7.2`
- `django-cloudinary-storage==0.3.0`
- `Pillow==8.2.0`
- `psycopg2==2.9.9`
- `dj-database-url==0.5.0`
- `django-allauth==0.54.0`
- `django-cors-headers==4.3.1`

You can find the full list of dependencies in the [requirements.txt](ForagingLink-API/requirements.txt)

---

## Deployment Instructions

1. **Forking or Cloning a Repository:**
   - **Forking:** Creates your own copy of the repository on your GitHub account.
     - Navigate to the chosen repository on GitHub.
     - Click the "Fork" button in the top-right corner.
     - For detailed instructions, check GitHub's documentation on [forking repositories](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo).
       <br>
   - **Cloning:** Downloads a copy of the repository to your local machine.
     - Open your Gitpod console.
     - Use the `git clone` command followed by the URL of the repository you wish to clone.
     - For detailed instructions, check GitHub's documentation on [cloning repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).
       <br>
2. **Cloudinary Account:**
   - Signup for a Cloudinary account on the [Cloudinary website](https://console.cloudinary.com/pm/c-22b4346b808568adb23133ede29fc9/getting-started).
   - Follow the instructions to sign up for an account and obtain your API key.
   - For more detailed instructions, check [Cloudinary's documentation](https://cloudinary.com/documentation).
     <br>
3. **Heroku Setup:**
   - Go to Heroku and sign up if you haven't already.
   - Create a new app from the Heroku dashboard.
   - Configure your app's settings, including region and environment variables.
   - Add the necessary environment variables:
     - CLOUDINARY_URL: Your Cloudinary URL.
     - DATABASE_URL: Your Postgres database URL.
     - SECRET_KEY: Generate a secret key for your Django project using a tool like [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/).
     - ALLOWED_HOSTS: URL of your API hosted on Heroku (without 'https://').
   - Heroku provides detailed documentation for each step of the setup process.
     <br>
4. **Database Configuration:**
   - Set up a PostgreSQL database instance with an appropriate provider. Some recommended options include:
     - [Heroku Postgres](https://www.heroku.com/postgres)
     - [AWS RDS for PostgreSQL](https://aws.amazon.com/rds/postgresql/)
     - [DigitalOcean Managed Databases](https://www.digitalocean.com/products/managed-databases/)
   - Ensure the instance meets your project's requirements, including region and plan selection.

### Note on ElephantSQL Service

Originally, this project used ElephantSQL for PostgreSQL hosting. However, ElephantSQL will discontinue its services on January 27, 2025. Due to this, an alternative PostgreSQL provider is necessary. The suggested options above should be explored further in order to find a suitable substitute. For more information on ElephantSQL's end of service, refer to their [End of Life Announcement](https://www.elephantsql.com/blog/end-of-life-announcement.html).

1. **Configuring Environment Variables:**
   - In your Heroku app settings, navigate to the "Config Vars" section.
   - Add the required environment variables:
     - CLOUDINARY_URL: Your Cloudinary URL.
     - DATABASE_URL: Your Postgres database URL from the provider you choose.
     - SECRET_KEY: Your generated secret key.
     - ALLOWED_HOSTS: URL of your API hosted on Heroku (without 'https://').
   - Ensure they are correctly set with the corresponding values.
   - [Heroku's documentation](https://devcenter.heroku.com/) provides detailed steps for managing environment variables.
     <br>
2. **Deployment:**
   - Choose GitHub as the deployment option in your Heroku dashboard.
   - Connect your repository and select the branch to deploy.
   - You can choose, enable automatic deploys for the main branch.
   - Once deployment is complete, you'll receive a link to your deployed site.
   - For more information on deploying applications to Heroku from GitHub, refer to Heroku's deployment documentation.

By following these steps and referring to the respective platform's documentation for detailed guidance, you should be able to successfully set up and deploy your API.

---

## Agile Development Approach

### Key Practices

1. **Iterative Development:**
   Building of the backend in a methodical, step-by-step way, ensuring that functions worked as expected before committing them and moving on.

2. **Regular Progress Tracking:**
   Not having a team with which I could have daily stand-ups to ensure a steady direction of travel with the development, I would use an A4 pad to summarize the day's achievements, check off the completed tasks that I'd created the day before, and create a plan and checklist for the next day after making an assessment of work completed.

3. **Task Management:**
   Developing the applications and the functions within them in a systematic manner based on the logical flow of dependencies. For example, starting with the Profiles app because it was the foundation that everything else would relate to. Then creating the Plants Blog app, which the Comments, Likes, and Followers apps depended on. The Courses and Course Registration apps, while within the main app, were not as directly linked to the other apps, so it was reasonable to leave them for last.

4. **Handling Unexpected Obstacles:**
   Changed how things were implemented when issues arose unexpectedly. For example, the pagination issue that I have described in detail.

5. **Exploring Solutions and Enhancements:**
   Initially followed a structure similar to the DRF-API walkthrough project, which focused on posts and comments. My intent was to create a subject-focused blog where only administrators could author posts while allowing users to comment on one another's contributions. This required a deeper understanding of the requirements and how to meet them effectively.

6. **Written Tests:**
   The writing of tests to ensure applications were functioning correctly. This process helped identify and resolve issues, such as adjusting the pagination settings to meet the specific requirements of the courses app. This issue, which did not initially affect the application's functionality, highlighted an aspect of the logic that needed refinement and more nuanced handling for the courses app.

7. **Reflective Development:**
   Regularly revisiting the naming conventions used across models and endpoints to ensure consistency and clarity, which enhanced maintainability.

8. **Continuous Integration and Documentation:**
   Documenting the backend structure for clarity and future reference. The "Models and CRUD Breakdown" section of the README outlines the functionality of each API endpoint. The Entity-Relationship Diagrams (ERDs) in the "Planning" section illustrate the database structure and relationships between models. Included docstrings in the code to provide insights into the structure and purpose of models, serializers, and views. For example, in `models.py`, each model has a detailed docstring explaining its purpose and relationships. Similarly, `views.py` and `serializers.py` files contain docstrings that explain the logic and functionality of each view and serializer, ensuring the code is well-documented and understandable.

### Examples of Agile Practices in Backend Development

#### Task Lists and Prioritization:

Managed tasks based on logical dependencies and the order in which lessons were followed, not strictly based on importance and urgency.

#### Adapting to Changes:

Adjusted plans as new requirements emerged or obstacles were encountered. For example, initially focusing on enabling comments on posts, but then adapting to allow users to comment on comments, adding complexity to the model and views to support nested comments.

#### Enhancing the Comments App:

Developed and refined the comments app by:

- Allowing users to comment on posts and reply to other comments.
- Ensuring comments were associated with users and posts.
- Implementing permissions to allow only authenticated users to create comments and only comment owners to update or delete their comments.

### Example Project Boards

The project boards were used to track the status of various tasks. Below are snapshots of the board showing tasks in different stages:

#### Starting State

Most tasks in the "ToDo" column.

![Most Tasks in the "ToDo" Column](https://res.cloudinary.com/cheymd/image/upload/v1718264077/forage/Foraging_API_README_images/Backlog_1_oh0hlx.png)

#### Midway State

More tasks moved to the "In Progress" column.

![More Tasks Moved to the "In Progress" Column](https://res.cloudinary.com/cheymd/image/upload/v1718264079/forage/Foraging_API_README_images/Backlog_2_akfbey.png)

#### Nearing Final State

Majority of tasks moved to the "Done" column.

![Majority of Tasks Moved to the "Done" Column](https://res.cloudinary.com/cheymd/image/upload/v1718264076/forage/Foraging_API_README_images/Backlog_3_wix3ap.png)

**Note (for the purpose of transparency):** These snapshots were taken when the tasks had in fact been completed and moved to the "Done" column. But to illustrate the workflow stages, the tasks were moved back into the "ToDo" and "In Progress" columns. This setup was used to visualize and manage the workflow effectively.

---

## Testing

### Written Tests

#### Tests for Plants Blog Application

Tests to verify that only an admin user can create a PlantInFocusPost instance and that a regular user can't.

[Plants Blog app tests](plants_blog/tests.py)

![Pass Screenshot](https://res.cloudinary.com/cheymd/image/upload/v1717385041/forage/Foraging_API_README_images/plants_blog_tests_irmprb.png)

#### Tests for Profiles Application

Tests to verify Creation, Update, and Deletion of a Profile instance given the appropriate permissions.

[Profiles app tests](profiles/tests.py)

![Pass Screenshot](https://res.cloudinary.com/cheymd/image/upload/v1717385041/forage/Foraging_API_README_images/profiles_tests_icrakl.png)

#### Tests for the Comments Application

Tests to ensure that a Like instance can be created and that the same instance be associated with either a PlantInFocus instance or a Comment instance, but not both Comments and a PlantInFocus at the same time.

[Comments app tests](comments/tests.py)

![Pass Screenshot](https://res.cloudinary.com/cheymd/image/upload/v1726204940/forage/Foraging_API_README_images/comments_tests_getldm.png)

#### Tests for the Likes Application

Tests for Creation, Deletion, and Unique Constraints of a Like Instance.

[Likes app tests](likes/tests.py)

![Pass Screenshot](https://res.cloudinary.com/cheymd/image/upload/v1717385041/forage/Foraging_API_README_images/likes_tests_lypugq.png)

#### Tests for Courses App

Tests to validate the functionality of the Course API views, including listing, creating, updating, and deleting courses, ensuring proper HTTP status codes are returned.
Handling Pagination in CourseList Tests
During the final testing phase, the tests for the Courses app started to fail due to global pagination settings applied in `settings.py`:
`"DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
"PAGE_SIZE": 10,`
These settings structured the response data with a results key, wrapping the list of courses and adding pagination metadata. The tests, which expected a simple list of courses, did not account for this change and failed. In reality, the test failing in this manner wasn't an indication of the application not working, but neither was it proof that it did.
To resolve this, the CourseList view was updated to handle the pagination structure properly by moving the queryset logic to its own function called get_queryset, which applied specific filters and ordering.
The tests were modified to work with the new paginated response. The response data now needed to be accessed within the results key. The tests were adjusted to check if there were any courses present in the results array before proceeding with further assertions. This ensured that the tests handled the paginated response structure correctly.

Defensive Programming
Initially, I thought that after creating a test course in the setup, it would always be present for the purpose of testing. I think it's a reasonable assumption. Under normal conditions, it's fair to assume that the test would pass. However, adding a check to see if the response contained a course instance before attempting to use it in the testing, swerved problems before they arose.

[Courses app tests](courses/tests.py)

![Pass Screenshot](https://res.cloudinary.com/cheymd/image/upload/v1717385041/forage/Foraging_API_README_images/courses_tests_tnodju.png)

### Tests for Course Registrations App

Tests to verify that a CourseRegistration instance can be created with all the necessary fields populated and that the default status of "Pending" is applied to new instances.

[Course Registrations app tests](course_registrations/tests.py)

![Pass Screenshot](https://res.cloudinary.com/cheymd/image/upload/v1717385040/forage/Foraging_API_README_images/course_registrations_uq9m5h.png)

---

## Future Developments

1. **User Messaging System**:

   - Adding a private messaging system for users to communicate with onneanther directly.

2. **Offline Mobile Application**:

   - Developing a mobile app that allows users to access certain features offline.
   - Using technologies like React Native for seamless integration with the existing React and DRF-API backend.

3. **User-Sourced Plant Sightings Map**:
   - Allowing users to mark locations on a map where they have found specific plants, along with pictures and notes.
   - Integration with Google Maps API.

_The User-Sourced Plant Sightings feature could be incorporated into the offline mobile app._

---

## Forking, Improving, Contributing

For detailed instructions on how to fork and clone a repository, please refer to GitHub's documentation:

- [How to Fork a Repository](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo)
- [How to Clone a Repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

### Making Your Changes

1. **Navigate to Your Project Directory:**

   Ensure that you're in your project's directory:

   - `cd path-to/your-project-directory`

2. **Create a New Branch:**

   Create a new branch for your changes:

   - `git checkout -b new-branch-name`

3. **Edit:**

   Make your changes to the code and save them.

4. **Commit:**

   Stage and commit your changes using:

   - `git add .`
   - `git commit -m "<Commit message for your changes>"`

5. **Push:**

   Push your changes to your forked repository:

   - `git push`

### Submit Pull Request

1. **Create Pull Request:**

   - Go to your fork on GitHub.
   - Click "New Pull Request."
   - Select the branch you created for your changes.
   - Create the pull request by providing a title and description of your changes.

2. **Review:**

   - Wait for response from owners of the project.
   - Make any requested changes.

3. **Merge:**

   - Once your changes are approved, your changes will be merged into the main project.

## Credits

- **StackOverflow:**

  - [Correctly retrieve data where date and time are greater than now](https://stackoverflow.com/questions/9549744/) for guidance on querying in Django.

- **StackOverflow**

  - [How to define two fields "unique" as couple](https://stackoverflow.com/questions/2201598/how-to-define-two-fields-unique-as-couple)

- **Django Documentation:**
  - [Django Queries](https://docs.djangoproject.com/en/5.0/topics/db/queries/) for understanding and implementing database queries.
- **Django REST Framework Documentation:**

  - [Django REST Framework API Guide](https://www.django-rest-framework.org/api-guide) for guidance on implementing API endpoints and understanding DRF concepts.

- **OpenAI's ChatGPT:**
  - For providing explanations, guidance on structuring the project, command line usage, and planning tools like Draw.io. The assistance included explanations on how to structure the README
  - Helped in creating virtual environments, explaining their importance, and resolving issues such as unsetting `PIP_USER` to install packages inside the virtual environment.
  - Advised on handling package version conflicts and ensuring compatibility.
