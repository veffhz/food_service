import json
from unittest.mock import patch, Mock

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

client = Client()


class GetAllRecipientsTest(TestCase):

    first_recipient = {
        'surname': 'Иванов',
        'name': 'Иван',
        'patronymic': 'Иванович',
        'phoneNumber': '8-999-777-66-00'
    }

    def setUp(self):
        patcher = patch('requests.get')
        self.mock_response = Mock(status_code=200)
        self.mock_response.raise_for_status.return_value = None

        with open('data_example/recipients.json', 'r') as f:
            self.mock_response.json.return_value = json.load(f)
        self.mock_request = patcher.start()
        self.mock_request.return_value = self.mock_response

    def test_get_all_recipients(self):
        response = client.get(reverse('recipients-list'))

        self.assertEqual(len(response.data), 15)
        self.assertEqual(response.data[0], GetAllRecipientsTest.first_recipient)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_recipient(self):
        response = client.get(reverse('recipient-detail', kwargs={'pk': 1}))

        self.assertEqual(response.data, GetAllRecipientsTest.first_recipient)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
