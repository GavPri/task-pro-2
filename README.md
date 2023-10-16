# Task Pro: Your Ultimate Task Management Solution

Welcome to **Task Pro**, your go-to Django application for seamless task management! Task Pro empowers users to efficiently create, read, update, and delete tasks in a secure and user-friendly environment. This application is designed to streamline your task management process, ensuring that you stay organized and focused on what matters most.

## Key Features:

1. **User Authentication:** Task Pro prioritizes the security of your tasks. Users must log in to access and manage their tasks, ensuring that your information remains private and confidential.

2. **CRUD Operations:** With Task Pro, you can easily perform CRUD (Create, Read, Update, Delete) operations on your tasks. Whether you need to add a new task, check its details, update its status, or remove it, Task Pro has got you covered.

3. **Intuitive User Interface:** The user interface is designed with simplicity and efficiency in mind. Navigate through your tasks effortlessly and focus on what needs to be done without any unnecessary complexity.

4. **Task Categories:** Organize your tasks by assigning them to specific categories. This feature allows you to group related tasks together, making it even easier to manage and prioritize your responsibilities.

5. **Responsive Design:** Task Pro is built with a responsive design, ensuring a seamless experience across various devices. Whether you're accessing it from a desktop, tablet, or smartphone, Task Pro adapts to your screen size for optimal usability.

## Task Templates

### Base Template (`base.html`)

The `base.html` template serves as the foundational structure for all pages in Task Pro, providing a consistent and visually appealing layout. Here's a breakdown of its key components:

#### Meta Information:

- **Charset:** The template specifies the character set as UTF-8 for proper encoding.
- **Google Fonts:** Utilizes the Google Fonts API to load the Oswald and Roboto font families for a modern and stylish appearance.
- **Bootstrap:** Integrates Bootstrap 5.3.2 for responsive and mobile-friendly design, ensuring a consistent look across different devices.
- **CSS:** Includes a custom stylesheet (`style.css`) located in the `static/css` directory to enhance the visual presentation.

#### Navigation Bar:

- **Logo Link:** The "Task Pro" logo in the navigation bar acts as a link. When the user is authenticated, it links to the task view (`view_tasks`), and when not authenticated, it links to the home page (`home`).
- **Toggle Button:** The navigation bar includes a toggle button for responsive design, allowing users to access navigation links on smaller screens.
- **User Authentication Links:** Depending on the user's authentication status, it provides links for signing out, signing up, or signing in.
- **Theme Toggle Button:** Features a button to toggle between light and dark themes, enhancing user customization.

#### Main Content:

- **Alert Messages:** Displays alert messages to provide feedback to the user. These messages are shown at the top of the page and automatically dismiss after a brief period.

#### Script References:

- **Bootstrap JavaScript:** Integrates the Bootstrap JavaScript bundle for enhanced functionality, such as the responsive navigation toggle.
- **FontAwesome:** Includes FontAwesome for the use of scalable vector icons.
- **Custom JavaScript:** Links to a custom JavaScript file (`app.js`) located in the `static/js` directory for additional custom functionality.

### Index (Home) Page Template (`index.html`)

The `index.html` template serves as the home page for Task Pro and extends the `base.html` template. Here's an overview of its key components:

#### Meta Information:

- The template extends the `base.html` template to maintain a consistent layout and styling throughout the application.
- Utilizes `{% load static %}` to load static files.

#### Content:

- **Hero Section (Non-authenticated users):** The hero section welcomes users to Task Pro and encourages them to log and track their tasks. It includes:
  - **Hero Text Container:** Contains the main text header and a brief description.
    - **Hero Text Header:** Displays the heading "Welcome To Task Pro."
    - **Hero Text Description:** Provides a subheading "Log and track your tasks."
    - **Sign In and Sign Up Buttons:** Links to the sign-in and sign-up pages (`{% url 'login' %}` and `{% url 'register_user' %}`) through visually appealing buttons.
  - **Hero SVG Wrapper:** Contains an SVG illustration representing the Task Pro concept.
    - **Hero SVG:** Displays an SVG image sourced from the `static/svg/task-pro-hero.svg` file.

### Task List Page Template (`task_list.html`)

The `task_list.html` template extends the `base.html` template and is responsible for displaying a tabbed interface to manage tasks. Here's an overview of its key components:

#### Meta Information:

- The template extends the `base.html` template to maintain a consistent layout and styling throughout the application.
- Utilizes `{% load static %}` to load static files.

#### Content:

- **Tabbed Interface Section (`tabbed-interface`):** The section displays a tabbed interface for different task categories.
  - **Add Task Button:** A button to navigate to the "Add A New Task" page.
  - **Category Headers:** Headers for different task categories: "All," "Urgent," and "Completed."
  - **Line Separator:** A visual separator line beneath the category headers.

- **Task Content Boxes:** Three boxes corresponding to each task category with the following structure:
  - **Content Box (All Tasks):** Displays all tasks.
  - **Content Box (Urgent Tasks):** Displays only urgent tasks.
  - **Content Box (Completed Tasks):** Displays only completed tasks.

Within each content box:
  - **Category Heading:** Heading indicating the category of tasks being displayed.
  - **Task List:** Lists tasks for the specific category.
    - **Task Title:** Displays the title of each task.
      - If the task is completed, the title has a strikethrough style.
    - **Task Icons:** Icons to update or delete each task.
    - **Task Description:** Describes the details of each task.

  - **Empty Message:** Displayed when there are no tasks in a specific category.

### Add Task Form Template (`add_task_form.html`)

The `add_task_form.html` template extends the `base.html` template and is responsible for rendering a form to add a new task in Task Pro. Here's an overview of its key components:

#### Meta Information:

- The template extends the `base.html` template to maintain a consistent layout and styling throughout the application.
- Utilizes `{% load static %}` to load static files.

#### Content:

- **Form Header:** Displays a visually appealing header indicating the purpose of the form: "Add A New Task."

- **Task Form:** A form element with the method set to "post" and the action pointing to the URL for adding a new task (`{% url 'add_task' %}`). This form includes the following input fields:
  - **Task Title:** A text input field (`<input>`) for entering the title of the task.
  - **Task Description:** A textarea input field (`<textarea>`) for entering a detailed description of the task.
  - **Urgent Checkbox:** A checkbox input (`<input type="checkbox">`) allowing users to mark the task as urgent.
  
- **Form Submission Button:** A "Submit" button (`<button>`) with the class "btn btn-primary" to submit the form.

### Edit Task Page Template (`edit_task.html`)

The `edit_task.html` template extends the `base.html` template and is used for editing an existing task. Here's an overview of its key components:

#### Meta Information:

- The template extends the `base.html` template to maintain a consistent layout and styling throughout the application.
- Utilizes `{% load static %}` to load static files.

#### Content:

- **Form Header Container:** Displays a container with a header indicating that the user is editing the task.
- **Edit Form:** A form allowing the user to edit the task details.
  - **Task Title Field:** An input field displaying the current task title and allowing the user to modify it.
  - **Task Description Field:** A textarea displaying the current task description and allowing the user to modify it.
  - **Urgent Checkbox:** A checkbox indicating whether the task is urgent. It is checked if the task is currently marked as urgent.
  - **Completed Checkbox:** A checkbox indicating whether the task is completed. It is checked if the task is currently marked as completed.
  - **Update Task Button:** A button to submit the form and update the task.

#### Edit Task Page Template (`edit_task.html`)

The `edit_task.html` template extends the `base.html` template and is used for editing an existing task. Here's an overview of its key components:

#### Meta Information:

- The template extends the `base.html` template to maintain a consistent layout and styling throughout the application.
- Utilizes `{% load static %}` to load static files.

#### Content:

- **Form Header Container:** Displays a container with a header indicating that the user is editing the task.
- **Edit Form:** A form allowing the user to edit the task details.
  - **Task Title Field:** An input field displaying the current task title and allowing the user to modify it.
  - **Task Description Field:** A textarea displaying the current task description and allowing the user to modify it.
  - **Urgent Checkbox:** A checkbox indicating whether the task is urgent. It is checked if the task is currently marked as urgent.
  - **Completed Checkbox:** A checkbox indicating whether the task is completed. It is checked if the task is currently marked as completed.
  - **Update Task Button:** A button to submit the form and update the task.

### Delete Task Page Template (`delete_task.html`)

The `delete_task.html` template extends the `base.html` template and is used for deleting a task. Here's an overview of its key components:

#### Meta Information:

- The template extends the `base.html` template to maintain a consistent layout and styling throughout the application.
- Utilizes `{% load static %}` to load static files.

#### Content:

- **Form Header Container:** Displays a container with a header indicating that the user is deleting the task.
- **Delete Form:** A form allowing the user to confirm the deletion of the task.
  - **Task Title Field:** An input field displaying the current task title (disabled and non-editable).
  - **Task Description Field:** A textarea displaying the current task description (disabled and non-editable).
  - **Urgent Checkbox:** A checkbox indicating whether the task is urgent. It is checked if the task is currently marked as urgent (disabled).
  - **Completed Checkbox:** A checkbox indicating whether the task is completed. It is checked if the task is currently marked as completed (disabled).
  - **Delete Button:** A button to submit the form and confirm the deletion of the task.

## Task Model

The `Task` model represents individual tasks in the Task Pro Django app. Here's an overview of the model's key attributes and functionalities:

### Fields:

- `user`: A foreign key relationship with the `User` model from Django's built-in authentication system. This establishes a connection between tasks and the user who created them.
- `title`: A character field with a maximum length of 255 characters, representing the title of the task.
- `description`: A text field that can be left blank (`null=True`) and is used for additional details about the task.
- `created_at`: A DateTime field set to auto-generate the current timestamp when a task is created (`auto_now_add=True`).
- `due_date`: A DateTime field that can be left blank (`null=True`), representing the due date of the task.
- `urgent`: A Boolean field with a default value of `False`, indicating whether the task is marked as urgent.
- `completed`: A Boolean field with a default value of `False`, indicating whether the task is marked as completed.

### Meta Class:

The `Meta` class within the model defines the default ordering for tasks. In this case, tasks are ordered by their creation date in descending order (`ordering = ['-created_at']`).

### String Representation:

The `__str__` method is implemented to provide a human-readable string representation of a task. In this case, it returns the title of the task.

This model enables the Task Pro app to store and manage tasks efficiently, associating each task with a user, capturing essential details, and allowing for sorting based on creation date.

## Task Views and URL Routing

This module defines various views and URL routing logic for the Task Pro Django app. Let's explore each view and its functionality:

### Home View (`home` function):

This view renders the home page (`index.html`) and is associated with the URL path `'/'`.

```python
from django.shortcuts import render

def home(request):
    return render(request, 'index.html') 
```

### Add Task View (`AddTaskView` class)

The `AddTaskView` class in Task Pro is responsible for handling the addition of new tasks. It is a class-based view that extends Django's `View` class. Let's break down its functionality:

#### Template Information:

- **Template Name:** The view uses the template named `add_task.html`.

#### Methods:

##### GET Method:

The `get` method is called when a user accesses the view using a GET request. It renders the `add_task.html` template, providing a form for users to add a new task.

```python
def get(self, request, *args, **kwargs):
    return render(request, self.template_name)
```
#### POST method: Handling Form Submission (`post` method)

The `post` method is a crucial part of the `AddTaskView` class and is invoked when a user submits the task addition form. Here's a breakdown of its functionality:

```python
def post(self, request, *args, **kwargs):
    # Process the form submission here
    title = request.POST.get('title')
    description = request.POST.get('description')
    urgent = request.POST.get('urgent', False) == 'on'
    completed = request.POST.get('completed', False) == 'on'

    # Create a new Task object
    task = Task(
        user=request.user,
        title=title,
        description=description,
        urgent=urgent,
        completed=completed
        )
    task.save()

    return redirect('view_tasks')
```
#### Steps:

1. **Form Data Extraction:**
   - The method retrieves form data from the request, including task title, description, urgency, and completion status.

2. **Task Object Creation:**
   - Using the extracted data, a new `Task` object is created.

3. **Database Saving:**
   - The newly created `Task` object is saved to the database, associating it with the current user.

4. **Redirect:**
   - After successfully adding the task, the user is redirected to the 'view_tasks' page.

This `post` method ensures a seamless and organized process for managing the addition of tasks within the Task Pro application.

## EditTaskView Class

The `EditTaskView` class is responsible for handling the editing of tasks in the Task Pro application. It follows the Django class-based views structure to provide a clean and organized approach to handle HTTP GET and POST requests for task editing.

#### GET Request Handling:

- **URL:** `/edit/<task_id>`
- **Method:** `GET`
- **Functionality:**
  - Retrieves the task from the database using the provided `task_id`.
  - Passes the task details to the template (`task_form.html`) for rendering the form.
  
#### POST Request Handling:

- **URL:** `/edit/<task_id>`
- **Method:** `POST`
- **Functionality:**
  - Retrieves the task from the database using the provided `task_id`.
  - Processes the form submission:
    - Updates the task's title, description, urgency, and completion status based on the submitted form data.
    - Saves the updated task to the database.
  - Redirects the user to the 'view_tasks' page after successfully updating the task.

This class ensures a smooth and structured process for users to edit tasks within the Task Pro application.
```python
class EditTaskView(View):
    template_name = 'task_form.html'

    def get(self, request, task_id, *args, **kwargs):
        # Retrieve the task from the database using the task_id
        task = get_object_or_404(Task, id=task_id)

        # Pass the task details to the template for rendering the form
        context = {
            'task': task,
        }

        return render(request, self.template_name, context)

    def post(self, request, task_id, *args, **kwargs):
        # Retrieve the task from the database using the task_id
        task = get_object_or_404(Task, id=task_id)

        # Process the form submission here
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.urgent = request.POST.get('urgent', False) == 'on'
        task.completed = request.POST.get('completed', False) == 'on'
        task.save()

        return redirect('view_tasks')
```
### DeleteTaskView Class

The `DeleteTaskView` class handles the deletion of tasks in the Task Pro application. It follows the Django class-based views structure to manage HTTP GET and POST requests related to task deletion.

#### GET Request Handling:

- **URL:** `/delete/<task_id>`
- **Method:** `GET`
- **Functionality:**
  - Retrieves the task from the database using the provided `task_id`.
  - Passes the task details to the template (`delete_task.html`) for confirmation.

#### POST Request Handling:

- **URL:** `/delete/<task_id>`
- **Method:** `POST`
- **Functionality:**
  - Retrieves the task from the database using the provided `task_id`.
  - Deletes the task from the database.
  - Redirects the user to the 'view_tasks' page after successfully deleting the task.

This class provides a well-organized and straightforward process for users to delete tasks within the Task Pro application.
```python
class DeleteTaskView(View):
    template_name = 'delete_task.html'

    def get(self, request, task_id, *args, **kwargs):
        # Retrieve the task from the database using the task_id
        task = get_object_or_404(Task, id=task_id)

        # Pass the task details to the template for confirmation
        context = {
            'task': task,
        }

        return render(request, self.template_name, context)

    def post(self, request, task_id, *args, **kwargs):
        # Retrieve the task from the database using the task_id
        task = get_object_or_404(Task, id=task_id)

        # Delete the task
        task.delete()

        return redirect('view_tasks')
```

## Task URLS

## Task Pro URL Configuration

The `urls.py` file defines the URL patterns for the Task Pro Django application. It maps different URLs to corresponding views, allowing users to navigate and interact with various functionalities of the application.

### URL Patterns:

1. **Home Page:**
   - URL: `/`
   - View: `home`
   - Name: `'home'`

2. **View Tasks:**
   - URL: `/tasks/`
   - View: `TaskListView.as_view()`
   - Name: `'view_tasks'`

3. **Add Task:**
   - URL: `/add/`
   - View: `AddTaskView.as_view()`
   - Name: `'add_task'`

4. **Edit Task:**
   - URL: `/edit/<task_id>`
   - View: `EditTaskView.as_view()`
   - Name: `'edit'`

5. **Delete Task:**
   - URL: `/delete/<task_id>`
   - View: `DeleteTaskView.as_view()`
   - Name: `'delete'`

### Usage:

- The URLs are used to define the navigation structure of the Task Pro application.
- They specify which views should be invoked for different user actions, such as viewing tasks, adding tasks, editing tasks, and deleting tasks.
- These URL patterns are then included in the main `urls.py` file of the Django project to integrate them into the overall project structure.

## Task View Testing

## Task Pro Unit Tests

This unit test file, `tests.py`, contains test cases for the Task Pro Django application. The tests are designed to verify the functionality of various views and user interactions within the application.

### Test Cases:

1. **Check Home Page Access:**
   - The `test_get_home_page` method verifies that anyone can access the home page (`/`). It checks the HTTP status code and the template used.

   ```python
   def test_get_home_page(self):
       response = self.client.get('/')
       self.assertEqual(response.status_code, 200)
       self.assertIn(
           'index.html', [template.name for template in response.templates])
    ```

2. **Check Access to Add Task View:**
   - The `test_view_access_to_add_when_logged_in` method ensures that logged-in users can access the 'view_tasks' page.

   ```python
   def test_view_access_to_add_when_logged_in(self):
       url = reverse('view_tasks')
       response = self.client.get(url)
       self.assertEqual(response.status_code, 200)
    ```

3. **Check Task Creation:**
   - The `test_create_task` method simulates a POST request to create a task and checks if the task is added to the database.

   ```python
   def test_create_task(self):
       url = reverse('add_task')
       response = self.client.post(url, {
           'title': 'Test Task',
           'description': 'This is a test task.',
           'urgent': 'on',
           'completed': 'on'
       })
       self.assertEqual(response.status_code, 302)
       redirect_url = reverse('view_tasks')
       self.assertEqual(response.url, redirect_url)
       self.assertTrue(
           Task.objects.filter(title='Test Task', user=self.user).exists())
    ```

4. **Check Access to Edit Task View:**
   - The `test_view_access_to_edit_when_logged_in` method checks if logged-in users can access the 'edit' view.

   ```python
   def test_view_access_to_edit_when_logged_in(self):
       self.task = Task.objects.create(user=self.user, title='Test Task')
       url = reverse('edit', args=[int(self.task.id)])
       response = self.client.get(url)
       self.task.delete()
       self.assertEqual(response.status_code, 200)
    ```

5. **Check Task Editing:**
   - The `test_edit_task` method simulates a POST request to edit a task and checks if the task details are updated in the database.

   ```python
   def test_edit_task(self):
       task = self.task
       url = reverse('edit', args=[str(self.task.id)])
       updated_title = 'Updated Test Task'
       updated_description = 'Updated description'
       response = self.client.post(url, {
           'title': updated_title,
           'description': updated_description,
           'urgent': 'on',
           'completed': 'on',
       })
       self.assertEqual(response.status_code, 302)
       redirect_url = reverse('view_tasks')
       self.assertEqual(response.url, redirect_url)
       task.refresh_from_db()
    ```

6. **Check Access to Delete Task View:**
   - The `test_view_access_to_delete_when_logged_in` method checks if logged-in users can access the 'delete' view.

    ```python
    def test_view_access_to_delete_when_logged_in(self):
       self.task = Task.objects.create(user=self.user, title='Test Task')
       url = reverse('delete', args=[int(self.task.id)])
       response = self.client.get(url)
       self.task.delete()
       self.assertEqual(response.status_code, 200)
    ```

7. **Check Task Deletion:**
   - The `test_delete_task` method simulates a POST request to delete a task and checks if the task is removed from the database.

   ```python
   def test_delete_task(self):
       self.task = Task.objects.create(user=self.user, title='Test Task')
       url = reverse('delete', args=[int(self.task.id)])
       response = self.client.get(url)
       self.assertEqual(response.status_code, 200)
       self.assertIn('task', response.context)
       response = self.client.post(url)
       self.assertEqual(response.status_code, 302)
       redirect_url = reverse('view_tasks')
       self.assertEqual(response.url, redirect_url)
       with self.assertRaises(Task.DoesNotExist):
           self.task.refresh_from_db()
    ```

#### Usage:

- Run the tests using the standard Django test runner.
- The tests cover various aspects of the Task Pro application, including view access, task creation, editing, and deletion.
- Ensure that the test data is cleaned up after each test to maintain a consistent test environment.

### Test Task Model:

This test case (`TestTaskModel`) is designed to ensure that the `Task` model in the Task Pro application behaves as expected, specifically focusing on the default values of the `urgent` and `completed` attributes.

#### Test Method: `test_urgent_defaults_to_false`

This method checks if the `urgent` attribute of a newly created `Task` defaults to `False`. The steps involved are as follows:

1. **Create a User:**
   - A test user (`user`) is created using `User.objects.create`.

2. **Create a Task:**
   - A new task (`task`) is created and associated with the test user, setting the title to 'Test model'.

3. **Assertion: `self.assertFalse(task.urgent)`**
   - This asserts that the `urgent` attribute of the task is `False`, ensuring it defaults to the expected value.

4. **Assertion: `self.assertFalse(task.completed)`**
   - Additionally, this asserts that the `completed` attribute of the task is also `False`, ensuring its default value.

This test is crucial to guarantee that when a new task is created, the `urgent` and `completed` attributes start with the correct default values.

```python
from django.contrib.auth.models import User
from django.test import TestCase
from .models import Task
import unittest

class TestTaskModel(unittest.TestCase):
    def test_urgent_defaults_to_false(self):
        # Create a user
        user = User.objects.create(username='Change Name 3')

        # Create a task associated with the user
        task = Task.objects.create(title='Test model', user=user)

        # Assert that urgent is False
        self.assertFalse(task.urgent)

        # Assert that completed is False
```