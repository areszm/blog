# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 15:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160517_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='document',
            name='title',
        ),
    ]
