# The Foraging API

## Project description

The **Foraging API** is a Django REST Framework Application Programming Interface for ["The Foraging Link"](https://github.com/CheyenneMDavid/foraging-link-ui), which serves as an online community, monthly foraging blog, and platform to promote seasonal foraging courses. It aims to connect people with nature and to one another whilst sharing information about the free edible delights available all around us.

## Table of Contents

- [The Foraging API](#the-foraging-api)
  - [Project description](#project-description)
  - [Table of Contents](#table-of-contents)
  - [User Stories](#user-stories)
    - [User Stories Clarification](#user-stories-clarification)
  - [Applications in the Project](#applications-in-the-project)
    - [Profiles](#profiles)
    - [Plants Blog](#plants-blog)
      - [Content of Individual Blog Post](#content-of-individual-blog-post)
    - [Comments](#comments)
    - [Likes](#likes)
    - [Followers](#followers)
    - [Courses](#courses)
    - [Course Registrations](#course-registrations)
      - [Dynamic Tracking of Course Spaces](#dynamic-tracking-of-course-spaces)
    - [Models and CRUD Breakdown](#models-and-crud-breakdown)
  - [Validation \& Data Integrity](#validation--data-integrity)
    - [Dietary Restrictions \& Emergency Contact Fields](#dietary-restrictions--emergency-contact-fields)
    - [Anonymization of Cancelled Registrations](#anonymization-of-cancelled-registrations)
  - [Planning](#planning)
    - [Entity-Relationship Diagrams (ERDs)](#entity-relationship-diagrams-erds)
    - [User Interaction and Authentication ERD](#user-interaction-and-authentication-erd)
    - [Course Management ERD](#course-management-erd)
    - [API Structure Diagrams](#api-structure-diagrams)
    - [User Interaction and Authentication Overview](#user-interaction-and-authentication-overview)
    - [Course Management](#course-management)
    - [Wireframes and Mockups](#wireframes-and-mockups)
  - [Explanation of Naming Decisions](#explanation-of-naming-decisions)
  - [Development Process](#development-process)
    - [Refining the User Story Table](#refining-the-user-story-table)
  - [Development Challenges \& Solutions](#development-challenges--solutions)
    - [Detail Page Like Count Discrepancy](#detail-page-like-count-discrepancy)
    - [Version Conflicts](#version-conflicts)
    - [Naming Conventions](#naming-conventions)
    - [Pagination Conflict in Courses App](#pagination-conflict-in-courses-app)
    - [Limiting Comment Nesting](#limiting-comment-nesting)
    - [Handling Comments and Replies](#handling-comments-and-replies)
    - [Field Name Update](#field-name-update)
    - [Database and Migration Issues](#database-and-migration-issues)
    - [Phone Number Validation](#phone-number-validation)
    - [Email Validation](#email-validation)
    - [CSRF Trusted Origins Issue and Legacy data](#csrf-trusted-origins-issue-and-legacy-data)
    - [Database Migration Reset and Cloudinary Path Adjustments](#database-migration-reset-and-cloudinary-path-adjustments)
    - [Counts for Likes and Comments](#counts-for-likes-and-comments)
    - [Logging for Debugging](#logging-for-debugging)
  - [Lessons Learned: Simple Fixes Can Be the Most Elusive](#lessons-learned-simple-fixes-can-be-the-most-elusive)
  - [Prerequisites](#prerequisites)
  - [Dependency Management](#dependency-management)
  - [Deployment Instructions](#deployment-instructions)
    - [Note on ElephantSQL Service](#note-on-elephantsql-service)
  - [Agile Development Approach](#agile-development-approach)
    - [Key Practices](#key-practices)
      - [Iterative Development](#iterative-development)
      - [Regular Progress Tracking](#regular-progress-tracking)
      - [Task Management](#task-management)
      - [Handling Unexpected Obstacles](#handling-unexpected-obstacles)
      - [Exploring Solutions and Enhancements](#exploring-solutions-and-enhancements)
      - [Reflective Development](#reflective-development)
      - [Continuous Integration and Documentation](#continuous-integration-and-documentation)
    - [Examples of Agile Practices in Backend Development](#examples-of-agile-practices-in-backend-development)
      - [Task Lists and Prioritization](#task-lists-and-prioritization)
      - [Adapting to Changes and Enhancements to the Applications](#adapting-to-changes-and-enhancements-to-the-applications)
    - [Example Project Boards](#example-project-boards)
      - [Starting State](#starting-state)
      - [Midway State](#midway-state)
      - [Nearing Final State](#nearing-final-state)
  - [Testing](#testing)
    - [Written Tests](#written-tests)
      - [Tests for Plants Blog Application](#tests-for-plants-blog-application)
      - [Tests for Profiles Application](#tests-for-profiles-application)
      - [Tests for the Comments Application](#tests-for-the-comments-application)
      - [Tests for the Likes Application](#tests-for-the-likes-application)
      - [Tests for the Followers App](#tests-for-the-followers-app)
      - [Tests for Courses App](#tests-for-courses-app)
    - [Tests for Course Registrations App](#tests-for-course-registrations-app)
  - [Future Developments](#future-developments)
  - [Forking, Improving, Contributing](#forking-improving-contributing)
    - [Making Your Changes](#making-your-changes)
    - [Submit Pull Request](#submit-pull-request)
  - [Credits](#credits)
    - [Email Validation: Source Reference](#email-validation-source-reference)
    - [Image Attribution](#image-attribution)
  - [Acknowledgment of AI Assistance](#acknowledgment-of-ai-assistance)

---

## User Stories

The user stories utilized in this project align with those listed in the associated frontend project. This decision was made because both frontend and backend components contribute to fulfilling these user stories, albeit in different capacities. The frontend is responsible for presenting information in the user interface, while the backend manages the storage and retrieval of data.

### User Stories Clarification

During the development process, user stories were initially tracked in GitHub projects, but over time, the table included in this README was developed to more accurately reflect the backend functionality. This table is based on a thorough review of the actual code, ensuring it aligns with the API endpoints and how each feature was implemented. As a result, this table provides a clearer, up-to-date representation of the backend user stories.

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

You can find the Project with fuller details for the [stories](https://github.com/users/CheyenneMDavid/projects/38/views/1)

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

The Comments app allows authenticated users to engage with posts and each other through a structured discussion format. Users can comment on posts and reply to other users' comments. To maintain clarity, nesting is limited to two levels.

### Likes

Likes enable users to express their appreciation for posts and comments. By liking content, they're able to show support for valuable contribution from one another. Unauthenticated users can see likes, but only authenticated users are able to add a like posts or comments

### Followers

The Followers app enables users to stay connected with content authors, including admins who create articles and users who contribute valuable comments. Only authenticated users can follow others.

### Courses

The Courses app is used to publish and manage upcoming courses in the seasons of spring, summer, and autumn. It allows all users, whether authenticated or not, to view course listings and details, while only admins have the ability to create, update, or delete courses. Each course detail page includes essential information such as the season, title, date, description, location, and maximum number of participants.

Within the Courses app, "the `UpComingCourse` view" returns courses with future dates, limiting the display to the 3 most immediate. Whilst "the `FullCourseList` view" returns all future courses, making them available for the front end.
Available spaces for the course are set to 10 by default and then managed by calculating the Maximum Capacity, minus the number of registrations.

### Course Registrations

The Course Registrations app manages user registrations for the courses offered. It allows users to register for courses and stores relevant information such as contact details, dietary restrictions, and emergency contact information.
Due to only authenticated users being able to submit a registration.

#### Dynamic Tracking of Course Spaces

The combination of the **Course Registration** app supplying the registrations and the **Courses** app validating the number of spaces allows dynamic tracking of the number of available spaces for each course. This ensures up to date information on space availability.

- **Available Spaces**: Each course has a predefined maximum number of participants. As users register for a course, the available spaces count is updated in real-time.

- **Automatic Update on Registration and Cancellation**: When a user registers for a course, one space is deducted from the total. If a user cancels their registration, the space is added back, keeping the count accurate.

- **Admin Panel View**: Admins can view the available spaces directly in the admin panel, making it easier to monitor course capacity and manage the registrations.

### Models and CRUD Breakdown

Although I have spoken about the individual applications within the project, the following table provides a quick reference allows a quicker understand the individual application's functionalities and their CRUD operations.

| Model              | Endpoints                                           | Create           | Retrieve | Update | Delete | Filter                                                                                                  | Text Search                                                                                             |
| ------------------ | --------------------------------------------------- | ---------------- | -------- | ------ | ------ | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| PlantInFocusPost   | /plants_blog/<br>/plants_blog/ :id/                 | Yes(Admins only) | Yes      | Yes    | Yes    | main_plant_name, main_plant_environment, culinary_uses, medicinal_uses, folklore, confusable_plant_name | main_plant_name, main_plant_environment, culinary_uses, medicinal_uses, folklore, confusable_plant_name |
| Comment            | /comments/<br>/comments/:id/                        | Yes              | Yes      | Yes    | Yes    | plant_in_focus_post, replying_comment, owner\_\_username                                                | content, owner**username, plant_in_focus_post**main_plant_name                                          |
| Like               | /likes/<br>/likes/:id                               | Yes              | Yes      | No     | Yes    | owner, plant_in_focus_post, comment                                                                     | None                                                                                                    |
| Follower           | /followers/<br>/followers/:id                       | Yes              | Yes      | No     | Yes    | None                                                                                                    | None                                                                                                    |
| Course             | /courses/<br>/courses/:id                           | Yes              | Yes      | Yes    | Yes    | None                                                                                                    | None                                                                                                    |
| CourseRegistration | /course_registrations/<br>/course_registrations/:id | Yes              | Yes      | No     | Yes    | None                                                                                                    | None                                                                                                    |

## Validation & Data Integrity

**Avatar Image Validation**:
In the Profiles application, avatar image validation has been implemented to balance high-quality profile pictures with backend efficiency:

- File Size: Avatar images are restricted to 2MB to prevent excessive storage and ensure the app's performance.

- Dimensions: The maximum size of 512 x 512 pixels keeps images sharp without using excessive space or loading time.

This validation ensures profile images are a reasonable size without becoming pixelated.

### Dietary Restrictions & Emergency Contact Fields

Validation logic in the `CourseRegistration` model ensures that if a user selects "Yes" for dietary restrictions or emergency contact, they must provide relevant details:

- **Dietary Restrictions**:

  If `has_dietary_restrictions` is True, then `dietary_restrictions` is required.

- **ICE - In Case of Emergency Contact**:

  If `has_emergency_contact` is True, `ice_name` and `ice_number` are required; if False, these fields must remain blank.

The conditional logic ensures that necessary information is provided only when relevant, improving data consistency.

### Anonymization of Cancelled Registrations

For canceled course registrations, personal data is anonymized to protect user privacy, whilst the rest is kept for possible analytics.

## Planning

### Entity-Relationship Diagrams (ERDs)

These diagrams show the structure and relationships of key components within the application that support user interaction and engagement.

### User Interaction and Authentication ERD

This shows the structure of the the applications's main models and their relationships within the application. It provides an overview of the models that facilitate users to engage with one another.
![User Interaction ERD](https://res.cloudinary.com/cheymd/image/upload/v1729046691/foraging_link/readme_images/user_interaction_and_authentication_erd_dvn9u9.png)

### Course Management ERD

This details the components involved in managing course content and user registrations submitted via contact forms. These are managed by site admins through the Django Admin Panel. This part of the application operates separately from the main user interaction features but is integrated within the same framework. It focuses on the relationships between Profiles, Courses, and Course Registrations.
![Course Management ERD](https://res.cloudinary.com/cheymd/image/upload/v1717661022/foraging_link/readme_images/course_management_erd_loozlc.png)

### API Structure Diagrams

These diagrams show the structure and relationships between the components in the Foraging Link API. They provide a visual representation of how users, posts, comments, likes, and followers interact within the system.

### User Interaction and Authentication Overview

This illustrates the user interaction and authentication structure within the Foraging Link API. It shows how users interact with comments, likes, blog posts, and followers, and includes the authentication component.
![User Interaction and Authentication](https://res.cloudinary.com/cheymd/image/upload/v1717661023/foraging_link/readme_images/user_interaction_and_authentication_overview_u3v4sf.png)

### Course Management

This Overview illustrates the course management structure within the Foraging Link API. It shows how users can read upcoming courses, fill out registration forms, and how admins can create and manage courses.
![Course Management Overview](https://res.cloudinary.com/cheymd/image/upload/v1717788223/foraging_link/readme_images/course_management_overview_nnmbfc.png)

### Wireframes and Mockups

Wireframes and Mockups can be found in a separate repository which handles [the React based User Interface](https://github.com/CheyenneMDavid/foraging-link-ui)

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

### Detail Page Like Count Discrepancy

**Cause of the Discrepancy:**

1. The LikeAndUnlike component on the detail page focused solely on the like_id (whether the user had liked the post) and did not initialize or maintain the total likes_count fetched from the backend.
2. The likes_count value was being overwritten dynamically during like/unlike actions instead of being updated while preserving the backend-provided total.

**Steps Taken to Resolve:**

1. Verified that the likes_count from the backend was correctly passed to the LikeAndUnlike component on the detail page by adding console logs with statements of what was beiong delivered for use in the front end.

2. Updated the LikeAndUnlike component to:
   - Initialize with the total likes_count fetched from the backend.
   - Dynamically update likes_count during like/unlike actions without overwriting the backend value.

### Version Conflicts

- Upgraded to a newer version of Django to use `django_filter` so that the admin panel could utilize advanced filtering for the comments application. A compromise was found by using Django 4.2 and the newer version of `django_filter` 24.2, which provided the advanced filtering capabilities. However, this caused huge compatibility issues elsewhere, so I reverted to `Django==3.2.4` and `django-filter==2.4.0`.

- Compatibility issues between Python 3.12 and `django-allauth` due to depreciated features in Python 3.12 required by `django-allauth`. This was resolved via tutor guidance on Slack as it was becoming a commonly experienced issue. The solution given was to install python version 3.9.19. This was a solution, but where I was using a virtual environment to isolate my dependencies, I found that I was having to reinstall the python version afresh each time I started my venv. Initially, I tried to add commands for older versions of python in the .bashrc file to avoid repetition of console commands. Unable to make the changes I realized that I lacked the permissions required. So instead, I created a script called `setup.sh`, hoping that this would allow me to enter a single command of: `./setup.sh`, but unfortunately, I couldn't seem to get it to create, start the virtual environment and load the requirements.txt as I needed, so I eventually resorted to entering the commands manually, again.

### Naming Conventions

- Inconsistent Use of Hyphens and Underscores: When creating the [Models and CRUD Breakdown](#models-and-crud-breakdown) table for this readme file and adding the search and filter fields to it, I noticed that I had been inconsistent in my use of hyphens and underscores. I decided to standardize the use of underscores in all URLs and updated the `urls.py` files in each app and any corresponding file across the entire codebase. As a result, all URL patterns now use underscores.

### Pagination Conflict in Courses App

- When initially writing the tests for the Courses app, all tests passed. However, during final testing, they started to fail. I traced the issue back to the implementation of global pagination settings in the main app's `settings.py` which I had copied from the DRF-API walkthrough project with Code Institute, because it was a good fit with the page structures. Specifically, these lines:
- `"DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
"PAGE_SIZE": 10,`
  However, these settings applied pagination structure to all list views, including the CourseList view. This changed the response data structure, placing the results within a results key and expecting 10 items per page due to this being globally set.
  This conflicted with the Courses app tests, which expected a simpler list of courses. The tests failed because they didn't account for the results key in the paginated response.
  For a detailed explanation of the solution, please refer to the [Testing](#testing) section and scroll to "Tests for courses app".

### Limiting Comment Nesting

- It was only when I was creating wireframes for the front end that I realized I had not placed a limit on the comments. As things stood, the nesting could have gotten out of hand. To guard against this, I added a restriction that limits comments to two levels, along with a test with the raising of a `ValueError` if a user attempts to create a third-level comment.

### Handling Comments and Replies

**Challenge**:

Comments and replies were not displaying correctly due to issues in API responses. Replies were missing, and the nesting structure needed refining.

**Solution**:

- Adjusted CommentSerializer to return full reply details instead of just IDs, reducing extra API calls.
- Limited nesting to two levels to maintain clarity and prevent excessive replies.
- Added replies_count as a read-only field in CommentSerializer to track the number of replies per comment.
- Ensured likes_count and replying_comment were properly included in serialized data for frontend use.
- Fixed queryset logic in views.py to correctly filter and return all comments and replies.

### Field Name Update

- While creating data to populate the database, I recognized that a more suitable field name for `folklore`
  in the `plants_blog` app was `history_and_folklore`. I updated the field name accordingly and brought all the other relevant files into alignment with the change.

### Database and Migration Issues

Significant challenges related to the database and migrations, often stemming from overcomplicating aspects of the backend and attempts to fix percieved issues.

**Key Issues Encountered**:
Unnecessary Model Changes: An attempt to add likes_count and comments_count directly to the PlantInFocusPost model created migration conflicts. These fields were present in the serializers.py and managed by the front end.

-
-
-
-

Accidental Deletion of Heroku Apps: While troubleshooting, both the backend and frontend Heroku apps were mistakenly deleted at different points, necessitating the creation of new apps and databases.
Migration Conflicts: Repeated migrations caused mismatched histories, leading to inconsistencies between the codebase and the database schema.
Data Loss: Missteps during migrations resulted in the loss of data, further complicating the debugging process.
Forking the Repository: Efforts to roll back changes by forking the repository and reverting to an earlier state added complexity without resolving the underlying issues.
Steps Taken to Resolve:
Rebuilding the Backend: A new Heroku backend app was created, and fresh migrations were applied after resetting the database schema.
Manual Data Restoration: Where possible, data was restored manually using backups or re-created in the admin panel.
Simplification: The likes_count and comments_count fields were removed from the model, and their logic was returned to the serializers, allowing the frontend to manage counts dynamically.
Refocusing on Core Functionality: Efforts were redirected toward ensuring the original intended features were restored, such as displaying posts and handling comments and likes effectively.
Key Takeaways:
Avoid Unnecessary Complexity: Trust existing functionality unless there is a clear need for change.
Backup Data Regularly: Backups are essential to mitigate the impact of data loss during troubleshooting.
Understand Dependencies: Changes to models should be carefully considered, as they can have far-reaching implications across the project.

### Phone Number Validation

Initially considered using REGEX to validate phone numbers within the
Course_Registrations application, but instead decided upon using the django-phonenumber-field package
which uses Google's phonenumbers library. This library, handles the validation and formatting of phone numbers based on regional standards. In this case, the region is set to ["GB" (ISO 3166-1 alpha-2 code)](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#GB).
This covered validation of both landlines and mobile number without the overly complex lines of code that REGEX would have created.

### Email Validation

Email validation for the CourseRegistration application is done using Django’s EmailValidator. It ensures the email inputed follows the expected format of an email address. The max_length is set to 254 characters, ensuring compatibility with most systems when handling email addresses. Validation takes place at the model level, ensuring the email is properly formatted before it's saved to the database.
Whilst the email is collected at the stage of signup, it plays no other part. This is purely to collect the address which allows it to be used by the front end when users are registering for a course.

During development, emails are printed to the console for testing only and are not actually delivered. It avoids accidently sending real emails, allowing email related features to be tested safely.

```python

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "optional"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```

### CSRF Trusted Origins Issue and Legacy data

After adding the new parts for user emails, I was left with legacy user data which still did not have this information. When I tried to update users, with the addition of an email address, I recieved: **403 Forbidden – CSRF verification failed.**

This error blocked changes made through the Django admin site. Although CORS_ALLOWED_ORIGINS and CORS_ALLOW_CREDENTIALS were correctly configured, this did not cover CSRF protection for POST requests from the admin panel.

The walkthrough used a similar configuration, but did not include explicit CSRF_TRUSTED_ORIGINS. In this project, we resolved the issue by adding the deployed API URL directly:

```python
Copy
Edit
CSRF_TRUSTED_ORIGINS = [
    "https://foraging-api-b287953c9098.herokuapp.com/",
]
```

This ensures Django trusts cross-origin POST requests from that specific domain, enabling admin edits (such as updating emails) without CSRF failures.

Guidance from:
<https://docs.djangoproject.com/en/3.2/ref/settings/#csrf-trusted-origins>

### Database Migration Reset and Cloudinary Path Adjustments

Initially, I organized my Cloudinary images into folders such as **Planning**, **Avatars**, and **Database Population** to keep the project’s media assets organized. However, this structure created issues when setting up the front end. The folder structure didn’t integrate well with the way images were accessed, so I decided to revert the Cloudinary upload and default image paths to a simpler setup.

This change led to complications with the database. Although I updated the image paths in the model fields, I encountered difficulties getting the database to reflect these new values correctly. This process required multiple attempts to adjust the Cloudinary paths, which led to a series of migrations that cluttered the migration history and still didn’t fully resolve the display issues with the default avatar image.

To provide a clean, working setup for assessment, I chose to reset the migrations and create a single, cohesive migration reflecting the final state of the models. The steps taken were:

1. **Path Adjustments for Cloudinary Avatar**: I experimented with different configurations for the Cloudinary avatar image path to ensure it would display correctly. Eventually, I simplified the setup by using only the Cloudinary public ID.

2. **Removing Previous Migration Files**: To eliminate migration clutter and start fresh, I deleted all existing migration files in each app’s `migrations` folder, except for the `__init__.py` file required by Django.

3. **Creating New Migrations**: With the Cloudinary configuration finalized, I ran `python manage.py makemigrations` to create a single, clean migration file for each app, reflecting the final state of the database models.

4. **Applying Migrations to the Database**: I applied these fresh migrations with `python manage.py migrate` to ensure the database schema matched the current models without any residual migration history.

5. **Database Reset**: Finally, I used `python manage.py flush` to clear out any data in the database, ensuring a clean slate with the newly structured schema.

I hoped that this reset process would allow me to resolve the problems, which I believed to be Cloudinary path issues.

However, after completing this entire reset, I discovered that the issue was not related to Cloudinary paths or migrations. The root cause was an incorrect string in the `USER_DETAILS_SERIALIZER` configuration in `settings.py`. Fixing this string by formatting it in a manner which passed PEP8 rules and also kept it in tact allowed the `profile_image` field to display correctly, making the previous efforts with migrations unnecessary.

### Counts for Likes and Comments

Whilst creating the front end, I found that the number of likes wasn’t displaying. After a lot of console logging, I realised that counts for likes and comments weren't included in the models for them. Previously including them in the Serializers.py files in both the Comments app and the Likes app, I had initially been following the structure of the walkthrough projects, but as I developed my individual applications, the manner in which the likes_count and comments_count were delivered to the React front end fell short. To fix this, I added the counts as properties, where their totals were then able to be dynamically calculated and made available for the React front end.

Additionally, the manner in which the imports were handled has been restructured, so as to avoid circular imports, and replies_count was added to the Comment model to dynamically track the number of nested replies.

### Logging for Debugging

When implementing the conditional display for the Most followed profiles, I had issues with the token refresh workinbg correctly. So additionally to adding console.logs throughout the front end's logic, I also added basic logging configuration to the settings.py

```python

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
}
```

## Lessons Learned: Simple Fixes Can Be the Most Elusive

After a journey through migration resets, Cloudinary path adjustments, and database reconfigurations, the final resolution turned out to be… a single misplaced string format in `settings.py`. Sometimes, even the smallest details can have us chasing our tails. Lesson learned: double-check the simple stuff!

The good news? At least we now have a perfectly clean migration history and a newfound respect for careful string formatting!

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
- `django-phonenumber-field==8.0.0`
- `Pillow==8.2.0`
- `psycopg2==2.9.9`
- `dj-database-url==0.5.0`
- `django-allauth==0.54.0`
- `django-cors-headers==4.3.1`

You can find the full list of dependencies in the [requirements.txt](requirements.txt)

---

## Deployment Instructions

1. **Forking or Cloning a Repository:**
   - **Forking:** Creates your own copy of the repository on your GitHub account.
     - Navigate to the chosen repository on GitHub.
     - Click the "Fork" button in the top-right corner.
     - For detailed instructions, check GitHub's documentation on [forking repositories](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo).
   - **Cloning**: Downloads a copy of the repository to your local machine.
     - Open your Gitpod console.
     - Use the `git clone` command followed by the URL of the repository you wish to clone.
     - For detailed instructions, check GitHub's documentation on [cloning repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).
2. **Cloudinary Account**:

   - Signup for a Cloudinary account on the [Cloudinary website](https://console.cloudinary.com/pm/c-22b4346b808568adb23133ede29fc9/getting-started).
   - Follow the instructions to sign up for an account and obtain your API key.
   - For more detailed instructions, check [Cloudinary's documentation](https://cloudinary.com/documentation).

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

#### Iterative Development

Building of the backend in a methodical, step-by-step way, ensuring that functions worked as expected before committing them and moving on.

#### Regular Progress Tracking

Not having a team with which I could have daily stand-ups to ensure a steady direction of travel with the development, I would use an A4 pad to summarize the day's achievements, check off the completed tasks that I'd created the day before, and create a plan and checklist for the next day after making an assessment of work completed.

#### Task Management

Developing the applications and the functions within them in a systematic manner based on the logical flow of dependencies. For example, starting with the Profiles app because it was the foundation that everything else would relate to. Then creating the Plants Blog app, which the Comments, Likes, and Followers apps depended on. The Courses and Course Registration apps, while within the main app, were not as directly linked to the other apps, so it was reasonable to leave them for last.

#### Handling Unexpected Obstacles

Changed how things were implemented when issues arose unexpectedly. For example, the pagination issue that I have described in detail.

#### Exploring Solutions and Enhancements

Initially followed a structure similar to the DRF-API walkthrough project, which focused on posts and comments. My intent was to create a subject-focused blog where only administrators could author posts while allowing users to comment on one another's contributions. This required a deeper understanding of the requirements and how to meet them effectively.

#### Reflective Development

Regularly revisiting the naming conventions used across models and endpoints to ensure consistency and clarity, which enhanced maintainability.

#### Continuous Integration and Documentation

Throughout the development process, I employed a continuous integration approach, regularly merging and testing features to ensure everything worked smoothly together. This iterative method allowed me to catch and fix issues as they arose.

The **Models and CRUD Breakdown** section of this README provides detailed information about the API endpoints, while **Entity-Relationship Diagrams (ERDs)** illustrate the relationships between models. I also ensured that **docstrings** were used consistently throughout the codebase, explaining the purpose and logic behind each model, view, and serializer, making the backend easier to understand and maintain.

Initially, I would have quite a lot of comments running through the code. The fulilled their purpose by explaining each bit. But also, where I myself was still learning, on one hand the comments I created explained well. But on the other hand, the lines of code that were the functional parts of the scripts where getting more and more disjointed. It was for this reason that I then opted for the comprehensive docstrings instead. This allowed me to better follow the flow and insert changes which where conditional logic, such as the issue of nested comments.

It was only upon reading discussions in Slack that I realised that a balance between docstrings and comments was necessary. Hence the later addisions of comments and the sunsequent changes during the reintroduction of coments.

### Examples of Agile Practices in Backend Development

#### Task Lists and Prioritization

Managed tasks based on logical dependencies and the order in which lessons were followed, not strictly based on importance and urgency.

#### Adapting to Changes and Enhancements to the Applications

Plans were adjusted as new requirements emerged or challenges were encountered. For instance, the initial goal was to enable users to comment on posts. However, I later expanded this functionality to allow users to comment on other comments, adding complexity to the models and views to support nested comments.

**In the Comments App**: One specific challenge was the unrestricted comment nesting, which initially allowed unlimited replies. After creating wireframes for the front end, I realized the need to limit nesting to two levels to maintain clarity and manageability of discussion threads. I implemented this restriction and then tested it to ensure proper functionality, raising appropriate ValidationErrors like "You cannot reply to a reply beyond two levels" to handle attempts at further nesting.

**In the Profiles App**: Another example is the **ProfileList search feature**, which I added to improve user engagement. By allowing users to search for specific profiles, the application encourages more meaningful interaction between users. This feature was thoroughly tested to ensure it worked seamlessly with the existing system.

**In the Courses App**: To allow unauthenticated users to view course details. Previously, this was restricted to authenticated users, but by allowing open access to course information, the app became more user-friendly and accessible to a broader audience.

PROJECT BOARDS

### Example Project Boards

The project boards were used to track the status of various tasks. Below are snapshots of the board showing tasks in different stages:

#### Starting State

Most tasks in the "ToDo" column.

![Most Tasks in the "ToDo" Column](https://res.cloudinary.com/cheymd/image/upload/v1718264077/foraging_link/readme_images/Backlog_1_oh0hlx.png)

#### Midway State

More tasks moved to the "In Progress" column.

![More Tasks Moved to the "In Progress" Column](https://res.cloudinary.com/cheymd/image/upload/v1718264079/foraging_link/readme_images/Backlog_2_akfbey.png)

#### Nearing Final State

Majority of tasks moved to the "Done" column.

![Majority of Tasks Moved to the "Done" Column](https://res.cloudinary.com/cheymd/image/upload/v1718264076/foraging_link/readme_images/Backlog_3_wix3ap.png)

**Note (for the purpose of transparency):** These snapshots were taken when the tasks had in fact been completed and moved to the "Done" column. But to illustrate the workflow stages, the tasks were moved back into the "ToDo" and "In Progress" columns. This setup was used to visualize and manage the workflow effectively.

---

## Testing

### Written Tests

Initially, basic tests were written for each application, and all tests passed successfully. However, during the development of the React frontend, I identified shortcomings in how counts for comments and likes were handled. These counts were managed solely on the frontend, with no corresponding values stored or fetched from the database. This approach, while functional in the lesson-based examples provided by Code Institute, proved inadequate as the project grew beyond the original lesson content. To address this, likes and comments counts were integrated into the backend, and tests were updated accordingly to validate these changes.

Additionally, database-related issues required starting afresh, which resulted in some migrations not being fully applied. To ensure the application's stability, I revisited and re-tested various aspects of the project. This process led to updates in models, tests, and migration files to align with the new backend functionality and resolve any inconsistencies.

#### Tests for Plants Blog Application

Tests to verify that only an admin user can create a PlantInFocusPost instance and that a regular user can't.
The tests confirm that a regular user attempting to perform this action receives a 403 Forbidden response, ensuring proper access control is enforced.

[Plants Blog app tests](plants_blog/tests.py)

![Pass Screenshot](https://res.cloudinary.com/cheymd/image/upload/v1736824991/foraging_link/readme_images/plants_blog_tests_tnozz5.png)

#### Tests for Profiles Application

Tests to verify Creation, Update, and Deletion of a Profile instance given the appropriate permissions.

[Profiles app tests](profiles/tests.py)

![Pass Screenshot](https://res.cloudinary.com/cheymd/image/upload/v1736824992/foraging_link/readme_images/profiles_tests_qzi86i.png)

#### Tests for the Comments Application

Tests to ensure that a Like instance can be created and that the same instance be associated with either a PlantInFocus instance or a Comment instance, but not both Comments and a PlantInFocus at the same time.

[Comments app tests](comments/tests.py)

![Pass Screenshot](https://res.cloudinary.com/cheymd/image/upload/v1736824990/foraging_link/readme_images/comments_tests_kgckwc.png)

#### Tests for the Likes Application

Tests for Creation, Deletion, and Unique Constraints of a Like Instance.

[Likes app tests](likes/tests.py)

![Pass Screenshot](https://res.cloudinary.com/cheymd/image/upload/v1736824991/foraging_link/readme_images/likes_tests_eeokls.png)

#### Tests for the Followers App

Tests were written to verify the creation and uniqueness of follower relationships between users. The FollowerModelTest ensures that a follower relationship can be created successfully and checks that duplicate relationships between the same users are not allowed. This is achieved through the UniqueConstraint defined in the model.

During testing, it was discovered that the UniqueConstraint hadn't been applied due to an earlier migration issue. To resolve this, the migration file was updated to include the constraint, and tests were re-run to confirm that duplicate relationships are now correctly prevented.

[Followers app tests](followers/tests.py)

![Pass Screenshot](https://res.cloudinary.com/cheymd/image/upload/v1736824991/foraging_link/readme_images/followers_tests_juskhi.png)

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

![Pass Screenshot](https://res.cloudinary.com/cheymd/image/upload/v1736824991/foraging_link/readme_images/courses_tests_geeuli.png)

### Tests for Course Registrations App

Tests to verify that a CourseRegistration instance can be created with all the necessary fields populated and that the default status of "Pending" is applied to new instances.

[Course Registrations app tests](course_registrations/tests.py)

Phone number validation added using `django-phonenumber-field` and Google's `phonenumbers` library. Re-tested with both mobile and landline number and passed.

![Pass Screenshot](https://res.cloudinary.com/cheymd/image/upload/v1736824991/foraging_link/readme_images/course_registrations_tests_tzpf9n.png)

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

- **Library Attributions**:

  - Google’s libphonenumber:

    - Phone numbers are validated by using uses Google’s libphonenumber library via the django-phonenumber-field package. It ensures proper formatting and validation of phone numbers based on regional standards.

  - django-phonenumber-field:
    - The django-phonenumber-field package simplifies handling phone numbers in Django applications by using Google’s phonenumbers library to validate and format phone numbers. The region is set to "GB" (ISO 3166-1 alpha-2 code), which you can [read more about](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#GB)

### Email Validation: Source Reference

Email validation was implemented using the following resources:

- **Django Documentation**:
  For email validation using `EmailValidator`, based on Django’s [EmailField documentation](https://docs.djangoproject.com/en/stable/ref/models/fields/#emailfield), which provides built-in validation mechanisms for email formats. Although when referencing this in `course_registrations/models.py` I left off the "#emailfield" as part of the url because I was unable to make the link work within the maximum line length.

- **RFC 5321**:
  For email length limit guidance, based on the [RFC 5321 standard](https://www.rfc-editor.org/rfc/rfc5321), which defines the 254-character limit for email addresses commonly used across the web.

### Image Attribution

- Some images used on this site are sourced from Pixabay, Pexels or similar free image sites.
- Any other images are original (taken by myself) or used with permission.
- The image of _Rumex obtusifolius_ is licensed under CC BY-SA 3.0. You can view the [original image](https://en.wikipedia.org/wiki/Rumex_obtusifolius#/media/File:Rumex-obtusifolius-foliage.JPG).
- All images are only displayed for the purpose of demonstrating the project.

## Acknowledgment of AI Assistance

Throughout the development of this project, I utilized OpenAI's ChatGPT for various aspects of the project, including planning, structuring tasks, and code-related queries. Discussions on prioritizing tasks and explanations and guidance for using third-party software in developing the project.

It proved to be a valuable resource for continuous feedback, task summarization, and resolving challenges along the way. I want to be fully transparent about how this tool was incorporated into my development process.

Some specific examples of how ChatGPT contributed to this project:

- **Task Summarization and Planning**: At the end of many work sessions, I used ChatGPT to summarize the day’s achievements and plan for the next steps. This helped me reflect on what was completed and prioritize the tasks for the following day. For example, we discussed how to proceed with the backend features like adding the comment nesting functionality and addressing pagination issues.

- **Conceptualization and Structuring**: ChatGPT helped in conceptualizing the project and refining my approach. One example is when we worked through the logic for **limiting comment nesting to two levels**. This feature was implemented after recognizing the need for clarity in comment threads and preventing excessive nesting.

- **Code Review and Problem Solving**: ChatGPT provided assistance when I encountered challenges in the code, such as the **pagination conflict** within the **Courses app**. The tool helped me identify and address the issue where global pagination settings conflicted with the app’s test cases, guiding me through the solution step by step.

- **Documentation Assistance**: I frequently used ChatGPT to help structure my README and user stories. This included discussions about how to better align my user stories with the backend functionality and how to represent changes in the API endpoints. The **user stories table** in the README reflects these discussions and revisions.

- **Use of Third-Party Tools**: ChatGPT provided instructions and guidance on how to utilize third-party tools like **Draw.io** for creating diagrams, such as **Entity-Relationship Diagrams (ERDs)**, which helped in planning and structuring the database models and relationships.

I believe that utilizing ChatGPT has enhanced my understanding of the development process and contributed to maintaining a clear focus throughout the project. While ChatGPT provided advice and assistance, all final decisions and implementations were done by me as part of my learning process.
