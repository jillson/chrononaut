# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_create_initial'),
        ('adventure', '0005_load_new_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='adventure',
            name='Map',
            field=models.ForeignKey(default=1, to='maps.Map'),
            preserve_default=False,
        ),
    ]
