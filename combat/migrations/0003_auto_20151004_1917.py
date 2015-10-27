# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('combat', '0002_auto_20151004_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character_class',
            name='Actions',
            field=models.ManyToManyField(to='combat.Class_Action', null=True),
        ),
        migrations.AlterField(
            model_name='pc',
            name='Equipment',
            field=models.ManyToManyField(to='core.ItemInstance', null=True),
        ),
    ]
