# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-17 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20170817_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameswitch',
            name='name',
            field=models.CharField(default='main', max_length=10),
        ),
    ]
