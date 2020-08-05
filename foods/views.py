from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from drf_yasg.utils import swagger_auto_schema, no_body
from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from foods.models import Recipient, ProductSets, Order
from foods.view_helper import (
    ProductFilter, CustomModelViewSet, OrderModelViewSet, OrderFilter
)
from foods.serializers import (
    RecipientSerializer, ProductSetsSerializer, OrderSerializer,
    RecipientFullNameSerializer, RecipientPhoneSerializer, OrderAddressSerializer
)


class RecipientViewSet(CustomModelViewSet):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer
    filter_backends = [OrderingFilter]
    ordering = ['id']

    @swagger_auto_schema(request_body=RecipientPhoneSerializer)
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = RecipientPhoneSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        super().perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    @action(detail=True, methods=['patch'])
    @swagger_auto_schema(request_body=RecipientFullNameSerializer)
    def change_full_name(self, request, pk=None):
        instance = self.get_object()
        serializer = RecipientFullNameSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = ProductSets.objects.all()
    serializer_class = ProductSetsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering = ['id']
    filterset_class = ProductFilter


class OrderViewSet(OrderModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = OrderFilter
    ordering = ['-id']

    @action(detail=True, methods=['patch'])
    @swagger_auto_schema(request_body=OrderAddressSerializer)
    def change_address(self, request, pk=None):
        instance = self.get_object()
        serializer = OrderAddressSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @action(detail=True, methods=['patch'])
    @swagger_auto_schema(request_body=no_body)
    def cancel(self, request, pk=None):
        instance = self.get_object()
        instance.cancel_order()
        return Response({'status': instance.status})

    @action(detail=True, methods=['patch'])
    @swagger_auto_schema(request_body=no_body)
    def process(self, request, pk=None):
        instance = self.get_object()
        instance.process_order()
        return Response({'status': instance.status})

    @action(detail=True, methods=['patch'])
    @swagger_auto_schema(request_body=no_body)
    def complete(self, request, pk=None):
        instance = self.get_object()
        instance.complete_order()
        return Response({'status': instance.status})
