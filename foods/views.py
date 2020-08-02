from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from foods.models import Recipient, ProductSets
from foods.serializers import RecipientSerializer, ProductSetsSerializer


class RecipientViewSet(ModelViewSet):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer


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
