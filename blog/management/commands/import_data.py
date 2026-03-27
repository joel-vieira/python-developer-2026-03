import json
import os

from django.core.management.base import BaseCommand
from django.db import transaction

from blog.models import Author, Post


DATA_INFORMATION = [
    {
        'model': Author,
        'directory_path': './data/authors/'
    },
    {
        'model': Post,
        'directory_path': './data/posts/'
    }
]

class Command(BaseCommand):
    help = 'Import authors and posts data from local json files to the database.'

    def handle(self, *args, **options):
        for data_information in DATA_INFORMATION:
            if not os.path.isdir(data_information['directory_path']):
                self.stderr.write(f"Could't find directory: {data_information['directory_path']}")
                return

            try:
                data = self.fetch_data_from_json(data_information['directory_path'])
                self.upload_to_database(data_information['model'], data)
            except Exception as e:
                self.stderr.write('Exiting because an error occurred.')
                return

        self.stdout.write('Data imported successfully!')

    def fetch_data_from_json(self, directory_path):
        data = []

        for file_name in os.listdir(directory_path):
            try:
                with open(directory_path + file_name, 'r') as data_file:
                    data.append(json.load(data_file))
            except FileNotFoundError as e:
                self.stderr.write(f"Could't find file: {directory_path + file_name}")
                raise e

        return data

    def upload_to_database(self, model, data):
        with transaction.atomic():
            for item in data:
                if 'author' in item.keys():
                    item['author_id'] = item.pop('author')

                try:
                    obj, created = model.objects.update_or_create(id=item['id'], defaults=item)
                except Exception as e:
                    self.stderr.write(f"Couldn't create {model.__name__}: {item['id']}")
                    raise e

                if created:
                    self.stdout.write(f"Successfully created {model.__name__}: {obj.id}")
                else:
                    self.stdout.write(f"Warning: {model.__name__} {obj.id} already exists!")
