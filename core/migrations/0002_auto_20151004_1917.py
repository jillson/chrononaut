# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='Inventory',
            field=models.ManyToManyField(to='core.ItemInstance', null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='State',
            field=models.ForeignKey(default=None, to='core.State', null=True),
        ),
    ]
