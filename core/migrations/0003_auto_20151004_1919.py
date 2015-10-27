# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151004_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='Inventory',
            field=models.ManyToManyField(to='core.ItemInstance', blank=True),
        ),
    ]
