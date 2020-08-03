from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework.decorators import action
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from foods.models import Recipient, ProductSets, Order
from foods.serializers import RecipientSerializer, ProductSetsSerializer, OrderSerializer, RecipientFullNameSerializer, \
    RecipientPhoneSerializer, OrderAddressSerializer


class RecipientViewSet(ModelViewSet):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer

    def update(self, *args, **kwargs):
        raise MethodNotAllowed(
            "PUT", detail="Use PATCH on <id>/change_full_name"
        )

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = RecipientPhoneSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        super().perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    @action(detail=True, methods=['patch'])
    def change_full_name(self, request, pk=None):
        instance = self.get_object()
        serializer = RecipientFullNameSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class ProductFilter(FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    min_weight = filters.NumberFilter(field_name="weight", lookup_expr='gte')

    class Meta:
        model = ProductSets
        fields = ['min_price', 'min_weight']


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = ProductSets.objects.all()
    serializer_class = ProductSetsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=True, methods=['patch'])
    def change_address(self, request, pk=None):
        instance = self.get_object()
        serializer = OrderAddressSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
