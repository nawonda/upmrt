# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-07 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20160407_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(max_length=6, null=True, verbose_name='gender'),
        ),
    ]