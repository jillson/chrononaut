# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=20)),
                ('Attribution', models.TextField()),
                ('Filename', models.CharField(max_length=40)),
                ('UnlockAmount', models.IntegerField(default=0)),
            ],
        ),
    ]
