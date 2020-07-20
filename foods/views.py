from django.http import HttpResponseBadRequest, Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from foods.api_helpers import get_recipients
from foods.api_helpers import get_foods, get_food_by_id


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
    foods = get_foods()

    if request.query_params:
        recipient_id = request.query_params.get('recipient_id')

        if not recipient_id:
            raise HttpResponseBadRequest

        return Response([])
    else:
        return Response(foods)


@api_view(http_method_names=['GET'])
def product_detail(request, pk):
    food = get_food_by_id(pk)

    if food:
        return Response(food)
    else:
        raise Http404
