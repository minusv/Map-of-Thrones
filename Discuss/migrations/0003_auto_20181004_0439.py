# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-03 23:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Discuss', '0002_auto_20181004_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='author',
            field=models.CharField(max_length=200),
        ),
    ]