from rest_framework.serializers import HyperlinkedModelSerializer

from foods.models import ProductSets, Recipient, Order


class ProductSetsSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ProductSets
        fields = [
            'id',
            'title',
            'description',
        ]


class RecipientSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Recipient
        fields = [
            'id',
            'name',
            'patronymic',
            'surname',
            'phone_number',
        ]


class OrderSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'order_created_datetime',
            'delivery_datetime',
            'delivery_address',
            'recipient',
            'product_set',
            'status'
        ]
