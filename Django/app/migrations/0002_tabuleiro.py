# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-07 19:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tabuleiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linha', models.CharField(max_length=2)),
                ('coluna', models.CharField(max_length=2)),
                ('status', models.BooleanField(default=False)),
                ('jogador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jogador', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]