import requests
from django.conf import settings

from foods.exceptions import RemoteServiceUnavailable


def get_recipients():
    return [_crop_recipient(recipient) for recipient in get_full_recipients()]


def get_full_recipients():
    try:
        return requests.get(settings.RECIPIENTS_API_URL).json()
    except requests.exceptions.RequestException:
        raise RemoteServiceUnavailable()


def get_full_products():
    try:
        return requests.get(settings.FOOD_API_URL).json()
    except requests.exceptions.RequestException:
        raise RemoteServiceUnavailable()


def get_products():
    return [_crop_product(product) for product in get_full_products()]


def get_product_by_id(pk):
    return next((_crop_product(product) for product in get_full_products()
                 if product['inner_id'] == pk), None)


def get_products_by_param(min_price, min_weight):
    products = get_products()

    if min_price and min_weight:
        return [
            product for product in products
            if product['price'] >= int(min_price) and product['weight'] >= int(min_weight)
        ]
    elif min_price:
        return [
            product for product in products if product['price'] >= int(min_price)
        ]
    else:
        return [
            product for product in products if product['weight'] >= int(min_weight)
        ]


def _crop_recipient(recipient):
    return {
        **recipient['info'],
        'phoneNumber': recipient['contacts']['phoneNumber'],
    }


def _crop_product(product):
    return {
        'title': product['name'],
        'description': product['about'],
        'price': product['price'],
        'weight': product['weight_grams'],
    }
