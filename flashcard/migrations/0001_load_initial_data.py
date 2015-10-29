# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.core.management import call_command

#http://stackoverflow.com/questions/25960850/loading-initial-data-with-django-1-7-and-data-migrations

fixture = 'load_flashcards'

def load_fixture(apps, schema_editor):
    call_command('loaddata', fixture, app_label='flashcard') 

def unload_fixture(apps, schema_editor):
    "Brutally deleting all entries for this model..."

    MyModel = apps.get_model("flashcard", "CardGenerator")
    MyModel.objects.all().delete()
    
class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [ migrations.RunPython(load_fixture, reverse_code=unload_fixture)
    ]
