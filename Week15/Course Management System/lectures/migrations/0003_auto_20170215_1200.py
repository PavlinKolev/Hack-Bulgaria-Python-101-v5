# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0002_auto_20170215_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
