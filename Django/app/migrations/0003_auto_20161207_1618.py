# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-07 19:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_tabuleiro'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tabuleiro',
            new_name='Posicao',
        ),
    ]
