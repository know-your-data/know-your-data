from django.db import models
from pathlib import Path
import os
import json

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

def link():
    with open(os.path.join(BASE_DIR, 'home/media/your_topics.json'), "r") as read_file:
        data = json.load(read_file)    

class SomeModel(models.Model):
    name = models.CharField(max_length=50)

# class MyModelName(models.Model):
#         """A typical class defining a model, derived from the Model class."""
#         my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')

# record = MyModelName(my_field_name="Instance #1")