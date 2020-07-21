from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from foods.api_helpers import get_recipients
from foods.api_helpers import (
    get_products, get_product_by_id, get_products_by_param
)


@api_view(http_method_names=['GET'])
def recipients_list(request):
    return Response(get_recipients())


@api_view(http_method_names=['GET'])
def recipient_detail(request, pk):
    recipients = get_recipients()

    if pk == 0 or pk >= len(recipients):
        raise Http404

    return Response(recipients[pk - 1])


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
