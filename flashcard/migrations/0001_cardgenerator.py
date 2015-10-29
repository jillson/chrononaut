# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardGenerator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Level', models.IntegerField(default=1)),
                ('Name', models.CharField(max_length=100)),
                ('Formula', models.TextField()),
                ('Question', models.TextField()),
            ],
        ),
    ]
