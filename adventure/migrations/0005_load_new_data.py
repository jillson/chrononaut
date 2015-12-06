# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.core.management import call_command

from django.contrib.auth.models import User
#http://stackoverflow.com/questions/25960850/loading-initial-data-with-django-1-7-and-data-migrations

fixture = 'new_adventure_calcutta'

def load_fixture(apps, schema_editor):
    primaryUser, created = User.objects.get_or_create(username="admin",password="admin",last_login="2015-11-24")
    if created:
        primaryUser.save()
    call_command('loaddata', fixture, app_label='adventure') 

def unload_fixture(apps, schema_editor):
    print "warning; skipping actions to undo this"
    pass
    
class Migration(migrations.Migration):

    dependencies = [ ('adventure', '0001_initial'),
                     ('adventure', '0002_auto_20151112_0401'),
                     ('adventure', '0003_load_initial_data'),
                     ('adventure', '0004_auto_20151112_0419'),
                     

    ]

    operations = [ migrations.RunPython(load_fixture, reverse_code=unload_fixture)
    ]
