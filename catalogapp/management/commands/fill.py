from django.core.management import BaseCommand

from catalogapp.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        product_list = [
            {'name': "Giant Panda",
             'description': "The giant panda is perhaps the most powerful symbol in the world when it comes to species conservation",
             'category': "1", 'price_for_one': '125'},
            {'name': "Red Panda",
             'description': "The red panda is slightly larger than a domestic cat with a bear-like body and thick russet fur.",
             'category': "2", 'price_for_one': '150'},
            {'name': "Qinling Panda",
             'description': "Qinling pandas are known to inhabit the Qin mountains of central China..",
             'category': "3", 'price_for_one': '120'},

        ]
        #for product in product_list:
         #   Product.objects.create(**product)
        product_for_create = []
        for product in product_list:
            product_for_create.append(Product(**product))

        Product.objects.bulk_create(product_for_create)