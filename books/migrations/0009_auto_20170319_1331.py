# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20170319_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowlist',
            name='return_date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='\u5f52\u8fd8\u65f6\u95f4'),
        ),
    ]