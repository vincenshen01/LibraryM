# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='', max_length=50, upload_to='books/%Y/%m', verbose_name='\u5c01\u9762\u56fe'),
        ),
    ]
