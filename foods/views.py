from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from foods.api_helpers import (
    get_products, get_product_by_id, get_products_by_param
)

from foods.models import Recipient
from foods.serializers import RecipientSerializer


class RecipientViewSet(ReadOnlyModelViewSet):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer


@api_view(http_method_names=['GET'])
def product_sets(request):
    if request.query_params:
        min_price = request.query_params.get('min_price')
        min_weight = request.query_params.get('min_weight')

        if not min_price and not min_weight:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(get_products_by_param(min_price, min_weight))
    else:
        return Response(get_products())


@api_view(http_method_names=['GET'])
def product_detail(request, pk):
    product = get_product_by_id(pk)

    if product:
        return Response(product)
    else:
        raise Http404
