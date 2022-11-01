import csv

from django.core.management.base import BaseCommand, CommandError

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:

            phone = Phone(name=phone['name'], image=phone['image'],
                          price=phone['price'],
                          release_date=phone['release_date'],
                          lte_exists=phone['lte_exists'],
                          slug=phone['name'].replace(' ', '-'))
            phone.save()



  # if phone['lte_exists'] == True:
            #     lte_exists = 'yes'
            # else:
            #     lte_exists = 'no'