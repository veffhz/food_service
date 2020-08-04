from django_filters import filters
from django_filters.rest_framework import FilterSet
from rest_framework import mixins
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.viewsets import GenericViewSet

from foods.models import ProductSets, StatusChoice, Order


class ProductFilter(FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    min_weight = filters.NumberFilter(field_name="weight", lookup_expr='gte')

    class Meta:
        model = ProductSets
        fields = ['min_price', 'min_weight']


class OrderFilter(FilterSet):
    start_date = filters.DateTimeFilter(
        field_name='order_created_datetime', lookup_expr='lt', input_formats=['%d-%m-%Y %H:%M']
    )
    end_date = filters.DateTimeFilter(
        field_name='order_created_datetime', lookup_expr='gt', input_formats=['%d-%m-%Y %H:%M']
    )
    date_range = filters.DateRangeFilter(field_name='order_created_datetime')
    status = filters.ChoiceFilter(field_name='status', choices=StatusChoice.choices())

    class Meta:
        model = Order
        fields = ['start_date', 'end_date', 'date_range', 'status']


class CustomModelViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.ListModelMixin,
                         GenericViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete', 'head']

    def update(self, *args, **kwargs):
        raise MethodNotAllowed("POST", detail="Use PATCH")


class OrderModelViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    http_method_names = ['get', 'post', 'patch', 'head']

    def update(self, *args, **kwargs):
        raise MethodNotAllowed("POST", detail="Use PATCH")
