from typing import Optional

import requests
from dataclasses import dataclass
from django.conf import settings

from foods.exceptions import RemoteServiceUnavailable, HttpBadRequest


@dataclass(frozen=True)
class Params:
    min_price: Optional[int]
    min_weight: Optional[int]


def get_recipients() -> list:
    return [_crop_recipient(recipient) for recipient in get_full_recipients()]


def get_full_recipients() -> list:
    try:
        return requests.get(settings.RECIPIENTS_API_URL).json()
    except requests.exceptions.RequestException:
        raise RemoteServiceUnavailable()


def get_full_products() -> list:
    try:
        return requests.get(settings.FOOD_API_URL).json()
    except requests.exceptions.RequestException:
        raise RemoteServiceUnavailable()


def get_products() -> list:
    return [_crop_product(product) for product in get_full_products()]


def get_product_by_id(pk: int) -> dict:
    return next((_crop_product(product) for product in get_full_products()
                 if product['inner_id'] == pk), None)


def get_products_by_param(min_price: str, min_weight: str) -> list:
    params = _parse(min_price, min_weight)

    if min_price:
        return [
            product for product in get_products()
            if product['price'] >= params.min_price
        ]
    else:
        return [
            product for product in get_products()
            if product['weight'] >= params.min_weight
        ]


def _parse(min_price: str, min_weight: str) -> Params:
    try:
        return Params(int(min_price) if min_price else None,
                      int(min_weight) if min_weight else None)
    except ValueError:
        raise HttpBadRequest()


def _crop_recipient(recipient: dict) -> dict:
    return {
        **recipient['info'],
        'phoneNumber': recipient['contacts']['phoneNumber'],
    }


def _crop_product(product: dict) -> dict:
    return {
        'title': product['name'],
        'description': product['about'],
        'price': product['price'],
        'weight': product['weight_grams'],
    }
