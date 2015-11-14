# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0003_load_initial_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adventure',
            name='UnlockTrigger',
            field=models.ForeignKey(blank=True, to='adventure.Adventure', null=True),
        ),
    ]
