from enum import Enum

from django.db import models


class ProductSets(models.Model):
    title = models.CharField('Наименование', max_length=50)
    description = models.TextField('Описание', blank=True)
    weight = models.PositiveIntegerField('Вес')
    price = models.PositiveIntegerField('Цена')

    def __str__(self):
        return f'{self.title}'


class Recipient(models.Model):
    surname = models.CharField('Фамилия', max_length=50)
    name = models.CharField('Имя', max_length=50)
    patronymic = models.CharField('Отчество', max_length=50, null=True, blank=True)
    phone_number = models.CharField('Телефон', max_length=20)

    def __str__(self):
        return f'{self.surname} {self.name}'


class StatusChoice(Enum):
    CREATED = 'created'
    DELIVERED = 'delivered'
    PROCESSED = 'processed'
    CANCELLED = 'cancelled'

    @classmethod
    def choices(cls):
        return [(status, status.value) for status in cls]


class Order(models.Model):
    order_created_datetime = models.DateTimeField(
        'Дата и время создания заказа', auto_now_add=True
    )

    delivery_datetime = models.DateTimeField(
        'Дата и время доставки', null=True
    )

    delivery_address = models.CharField('Адрес доставки', max_length=50)

    recipient = models.ForeignKey(Recipient, verbose_name='Получатель',
                                  related_name='orders', on_delete=models.CASCADE)

    product_set = models.ForeignKey(ProductSets, verbose_name='Набор продуктов',
                                    related_name='orders', on_delete=models.CASCADE)

    status = models.CharField('Статус', max_length=20, default=StatusChoice.CREATED,
                              choices=StatusChoice.choices())

    def __str__(self):
        return f'Заказ {self.pk}'
