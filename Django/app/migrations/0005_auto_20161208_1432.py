# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-08 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20161207_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posicao',
            name='status',
            field=models.CharField(max_length=1),
        ),
    ]
