# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160927_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='prurl',
            field=models.URLField(blank=True, db_index=True, null=True, verbose_name=b'Pull request URL'),
        ),
    ]
