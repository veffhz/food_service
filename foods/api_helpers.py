import requests
from django.conf import settings


def get_recipients():
    response = requests.get(settings.RECIPIENTS_API_URL)
    return [crop_recipient(recipient) for recipient in response.json()]


def get_full_recipients():
    response = requests.get(settings.RECIPIENTS_API_URL)
    return [recipient for recipient in response.json()]


def get_foods():
    response = requests.get(settings.FOOD_API_URL)
    return [crop_food(recipient) for recipient in response.json()]


def get_full_foods():
    response = requests.get(settings.FOOD_API_URL)
    return [recipient for recipient in response.json()]


def get_food_by_id(pk):
    return next((crop_food(food) for food in get_full_foods()
                 if food['inner_id'] == pk), None)


def crop_recipient(recipient):
    return {
        **recipient['info'],
        'phoneNumber': recipient['contacts']['phoneNumber'],
    }


def crop_food(food):
    return {
        'title': food['name'],
        'description': food['about'],
    }
