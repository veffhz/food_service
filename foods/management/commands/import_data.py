import json

from django.core.management.base import BaseCommand

from foods.models import ProductSets, Recipient


RECIPIENTS_FILE = 'foods/data/recipients.json'
FOOD_BOXES_FILE = 'foods/data/foodboxes.json'


class Command(BaseCommand):
    help = 'Master data import'

    def handle(self, *args, **options):
        run()


def run():

    with open(RECIPIENTS_FILE, 'r') as f:
        recipients = json.load(f)

        for recipient in recipients:

            Recipient.objects.create(
                surname=recipient['info']['surname'],
                name=recipient['info']['name'],
                patronymic=recipient['info']['patronymic'],
                phone_number=recipient['contacts']['phoneNumber'],
            )

    with open(FOOD_BOXES_FILE, 'r') as f:
        food_boxes = json.load(f)

        for food_box in food_boxes:

            ProductSets.objects.create(
                weight=food_box['weight_grams'],
                price=food_box['price'],
                title=food_box['name'],
                description=food_box['about'],

            )
