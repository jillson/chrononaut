# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.core.management import call_command

fixture = 'load_maps_1'

def load_fixture(apps, schema_editor):
    call_command('loaddata', fixture, app_label='maps') 

def unload_fixture(apps, schema_editor):
    "Brutally deleting all entries for this model..."

    Maps = apps.get_model("maps", "Map")
    Maps.objects.all().delete()
    
class Migration(migrations.Migration):

    dependencies = [ ('maps', '0001_initial'),
    ]

    operations = [ migrations.RunPython(load_fixture, reverse_code=unload_fixture)
    ]
