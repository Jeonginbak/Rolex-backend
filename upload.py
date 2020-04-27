import os
import django
import csv
import sys

os.chdir(".")
print("Current dir=", end=""), print(os.getcwd())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR=", end=""), print(BASE_DIR)

sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rolex.settings")
django.setup()

from product.models import *

CSV_PATH = './rolex_csv/size.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        Size.objects.create(
            size = row['size'],
            )

CSV_PATH = './rolex_csv/material.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        Material.objects.create(
            color          = row['name'],
            image_url      = row['image_url'],
            background_url = row['background_url']
            )