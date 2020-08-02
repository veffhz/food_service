from django.urls import reverse
from rest_framework import status
from django.test import TestCase, Client

from foods.models import Recipient, ProductSets
from foods.serializers import RecipientSerializer, ProductSetsSerializer

client = Client()


class RecipientsTest(TestCase):

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
        response = client.get(reverse('foods:recipient-list'))

        recipients = Recipient.objects.all()
        serializer = RecipientSerializer(recipients, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_recipient(self):
        response = client.get(reverse(
            'foods:recipient-detail', kwargs={'pk': self.first_recipient.pk}
        ))

        recipient = Recipient.objects.get(pk=self.first_recipient.pk)
        serializer = RecipientSerializer(recipient)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetProductsTest(TestCase):
    def setUp(self):
        self.first_product = ProductSets.objects.create(
            title='Семейная промо-коробка',
            description=('Набор продуктов на каждый день. Если надоело думать над составом заказа, '
                         'или вы у нас первый раз — это отличный выбор. Из этих продуктов можно '
                         'приготовить больше 10 блюд на завтрак, обед или ужин. Сорта продуктов '
                         'могут меняться, в зависимости от наличия товаров.'),
            price=3000,
            weight=9200
        )
        self.second_product = ProductSets.objects.create(
            title='Фруктовая промо-коробка',
            description=('Лучший вариант для первого заказа - коробка-сюрприз. '
                         'В составе один крупный фрукт, несколько видов сезонных и экзотических фруктов, '
                         'а также сухофрукты либо сладости.'),
            price=2400,
            weight=4500
        )

    def test_get_all_products(self):
        response = client.get(reverse('foods:product-list'))

        product_sets = ProductSets.objects.all()
        serializer = ProductSetsSerializer(product_sets, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_products_with_price(self):
        response = client.get(reverse('foods:product-list') + '?min_price=2500')

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_products_with_weight(self):
        response = client.get(reverse('foods:product-list') + '?min_weight=5000')

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_product(self):
        response = client.get(reverse(
            'foods:product-detail', kwargs={'pk': self.first_product.pk}
        ))

        product_set = ProductSets.objects.get(pk=self.first_product.pk)
        serializer = ProductSetsSerializer(product_set)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
