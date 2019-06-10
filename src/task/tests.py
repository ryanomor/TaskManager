from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from task.models import TaskItem
import datetime

# Create your tests here.
def createItem(client):
    url = reverse('taskitem-list')
    data = {
        'title': 'Take out the trash',
        'description': 'Take out the trash',
        'due_date': datetime.date.today()
        }
    return client.post(url, data, format='json')

class TestCreateTaskItem(APITestCase):
    """
    Ensure we can create a new task item
    """

    def setUp(self):
        self.response = createItem(self.client)

    def test_received_201_created_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_received_location_header_hyperlink(self):
        self.assertRegexpMatches(self.response['Location'], '^http://.+/tasks/[\d]+$')

    def test_item_was_create(self):
        self.assertEqual(TaskItem.objects.count(), 1)
    
    def test_item_has_correct_title(self):
        self.assertEqual(TaskItem.objects.get().title, 'Take out the trash')

class TestUpdateTaskItem(APITestCase):  
    """
    Checks we can update an existing Task item using PUT
    """

    def setUp(self):
        response = createItem(self.client)
        self.assertEqual(TaskItem.objects.get().completed, False)
        url = response['Location']
        data = {'title': 'Take out the trash', 'completed': True}
        self.response = self.client.put(url, data, format='json')

    def test_received_200_created_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_item_was_updated(self):
        self.assertEqual(TaskItem.objects.get().completed, True)

class TestPatchTaskItem(APITestCase):
    """
    Checks we can update an existing Task item using PATCH
    """

    def setUp(self):
        response = createItem(self.client)
        self.assertEqual(TaskItem.objects.get().completed, False)
        url = response['Location']
        data = {'title': 'Take out the trash', 'completed': True}
        self.response = self.client.patch(url, data, format='json')

    def test_received_200_created_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_item_was_patched(self):
        self.assertEqual(TaskItem.objects.get().completed, True)

class TestDeleteTaskItem(APITestCase):
    """
    Checks we can delete an existing Task item
    """

    def setUp(self):
        response = createItem(self.client)
        self.assertEqual(TaskItem.objects.get().completed, False)
        url = response['Location']
        data = {'title': 'Take out the trash', 'completed': True}
        self.response = self.client.delete(url)

    def test_received_204_no_content_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)

    def test_item_was_deleted(self):
        self.assertEqual(TaskItem.objects.count(), 0)

class TestDeleteAllItems(APITestCase):
    """
    Checks we can delete an existing Task item
    """

    def setUp(self):
        createItem(self.client)
        createItem(self.client)
        self.assertEqual(TaskItem.objects.count(), 2)
        self.response = self.client.delete(reverse('taskitem-list'))

    def test_received_204_no_content_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)

    def test_all_items_deleted(self):
        self.assertEqual(TaskItem.objects.count(), 0)
