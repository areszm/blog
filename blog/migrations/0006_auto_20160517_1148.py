# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160516_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.ImageField(blank=True, null=True, upload_to='documents/%Y/%m/%d'),
        ),
    ]
