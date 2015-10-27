# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('combat', '0004_auto_20151004_1919'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CardGenerator',
        ),
    ]
