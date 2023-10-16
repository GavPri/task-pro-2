import unittest
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task


class TaskListViewTest(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.client = Client()
        # Creating a test user
        self.user = User.objects.create_user(
            username='testuser3', password='testpassword')
        # Log the user in
        self.client.login(username='testuser3', password='testpassword')
        # Create a task
        self.task_id = 1

    # Check That Anyone Can Access The Home Page
    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # Manually check the template used
        self.assertIn(
            'index.html', [template.name for template in response.templates])

    # Check That Logged In Users Can Access The Add Task Views
    def test_view_access_to_add_when_logged_in(self):
        url = reverse('view_tasks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_task(self):
        url = reverse('add_task')
        # Simulate a POST request to create a task
        response = self.client.post(url, {
            'title': 'Test Task',
            'description': 'This is a test task.',
            'urgent': 'on',  # Simulating a checkbox being checked
            'completed': 'on'  # Simulating a checkbox being checked
        })

        # Check if the task was created successfully
        self.assertEqual(response.status_code, 302)
        redirect_url = reverse('view_tasks')

        # Check if the response redirects to the expected URL
        self.assertEqual(response.url, redirect_url)

        # Check if the task was actually created in the database
        self.assertTrue(
            Task.objects.filter(title='Test Task', user=self.user).exists())

    # Check That Logged In Users Can Access The Edit Task Views
    def test_view_access_to_edit_when_logged_in(self):
        # Create a task before attempting to access the 'edit' view
        task = Task.objects.create(user=self.user, title='Test Task')

        url = reverse('edit', args=[str(task.id)])
        response = self.client.get(url)

        # Clean up the created task after the test
        task.delete()

        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        # Clean up any test data as needed
        self.user.delete()


# This guard ensures that the test case is only run when the script is executed
if __name__ == '__main__':
    unittest.main()
