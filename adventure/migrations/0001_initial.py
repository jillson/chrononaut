# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Adventure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=20)),
                ('Description', models.TextField()),
                ('Lat', models.CharField(default=b'-30', max_length=20)),
                ('Lng', models.CharField(default=b'-30', max_length=20)),
                ('Distance', models.IntegerField(default=1000)),
                ('UnlockTrigger', models.ForeignKey(to='adventure.Adventure', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AdventureInstances',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Adventure', models.ForeignKey(to='adventure.Adventure')),
                ('Player', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UnlockStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Value', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='adventureinstances',
            name='State',
            field=models.ForeignKey(to='adventure.UnlockStatus'),
        ),
    ]
