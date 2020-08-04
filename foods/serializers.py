from phonenumbers import parse, is_valid_number, NumberParseException
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from foods.models import ProductSets, Recipient, Order


class ProductSetsSerializer(ModelSerializer):
    class Meta:
        model = ProductSets
        fields = [
            'id',
            'title',
            'description',
            'price',
            'weight'
        ]


class RecipientSerializer(ModelSerializer):
    def validate_phone_number(self, value): # noqa
        try:
            phone = parse(value, 'RU')
            if not is_valid_number(phone):
                raise NumberParseException(phone, '')
        except NumberParseException:
            raise serializers.ValidationError(f'{value} неверный формат номера!')
        return value

    class Meta:
        model = Recipient
        fields = [
            'id',
            'name',
            'patronymic',
            'surname',
            'phone_number',
        ]


class RecipientFullNameSerializer(ModelSerializer):
    class Meta:
        model = Recipient
        fields = [
            'name',
            'patronymic',
            'surname',
        ]


class RecipientPhoneSerializer(RecipientSerializer):
    class Meta(RecipientSerializer.Meta):
        fields = [
            'phone_number',
        ]


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        read_only_fields = ['status', 'order_created_datetime', 'delivery_datetime']
        fields = [
            'id',
            'order_created_datetime',
            'delivery_datetime',
            'delivery_address',
            'recipient',
            'product_set',
            'status',
        ]


class OrderAddressSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'delivery_address',
        ]
