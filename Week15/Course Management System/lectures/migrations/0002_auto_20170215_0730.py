# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='week',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
