import json
from unittest.mock import patch, Mock

from django.urls import reverse
from rest_framework import status
from django.test import TestCase, Client

from foods.models import Recipient
from foods.serializers import RecipientSerializer

client = Client()


class GetRecipientsTest(TestCase):

    def setUp(self):
        self.first_recipient = Recipient.objects.create(
            surname='Иванов',
            name='Иван',
            patronymic='Иванович',
            phone_number='8-999-777-66-00'
        )
        self.second_recipient = Recipient.objects.create(
            surname='Малейкина',
            name='Лолита',
            patronymic='Петровна',
            phone_number='8-919-457-36-60'
        )

    def test_get_all_recipients(self):
        response = client.get(reverse('recipient-list'))

        recipients = Recipient.objects.all()
        serializer = RecipientSerializer(recipients, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_recipient(self):
        response = client.get(reverse(
            'recipient-detail', kwargs={'pk': self.first_recipient.pk}
        ))

        recipient = Recipient.objects.get(pk=self.first_recipient.pk)
        serializer = RecipientSerializer(recipient)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetAllProductsTest(TestCase):

    first_product = {
        'title': 'Семейная промо-коробка',
        'description': ('Набор продуктов на каждый день. Если надоело думать над составом заказа, '
                        'или вы у нас первый раз — это отличный выбор. Из этих продуктов можно '
                        'приготовить больше 10 блюд на завтрак, обед или ужин. Сорта продуктов '
                        'могут меняться, в зависимости от наличия товаров.'),
        'price': 3000,
        'weight': 9200
    }

    def setUp(self):
        patcher = patch('requests.get')
        self.mock_response = Mock(status_code=200)
        self.mock_response.raise_for_status.return_value = None

        with open('foods/data/foodboxes.json', 'r') as f:
            self.mock_response.json.return_value = json.load(f)
        self.mock_request = patcher.start()
        self.mock_request.return_value = self.mock_response

    def test_get_all_products(self):
        response = client.get(reverse('product-sets'))

        self.assertEqual(len(response.data), 15)
        self.assertEqual(response.data[0], GetAllProductsTest.first_product)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_products_with_price(self):
        response = client.get(reverse('product-sets') + '?min_price=2000')

        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_products_with_weight(self):
        response = client.get(reverse('product-sets') + '?min_weight=5000')

        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_product(self):
        response = client.get(reverse('product-detail', kwargs={'pk': 1}))

        self.assertEqual(response.data, GetAllProductsTest.first_product)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
