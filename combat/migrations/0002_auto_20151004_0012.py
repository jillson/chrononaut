# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('combat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Battle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=80)),
                ('HumanLead', models.ForeignKey(to='core.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Character_Class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Class_Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(default=b'Sammy Do!', max_length=100)),
                ('HP', models.IntegerField()),
                ('HP_Max', models.IntegerField()),
                ('XP', models.IntegerField(default=0)),
                ('Level', models.IntegerField(default=1)),
                ('Active', models.BooleanField(default=False)),
                ('Equipment', models.ManyToManyField(to='core.ItemInstance')),
                ('Owner', models.ForeignKey(to='core.Player', null=True)),
                ('PClass', models.ForeignKey(to='combat.Character_Class')),
            ],
        ),
        migrations.AddField(
            model_name='character_class',
            name='Actions',
            field=models.ManyToManyField(to='combat.Class_Action'),
        ),
        migrations.AddField(
            model_name='battle',
            name='Team1',
            field=models.ManyToManyField(related_name='friends', to='combat.PC'),
        ),
        migrations.AddField(
            model_name='battle',
            name='Team2',
            field=models.ManyToManyField(related_name='enemies', to='combat.PC'),
        ),
    ]
