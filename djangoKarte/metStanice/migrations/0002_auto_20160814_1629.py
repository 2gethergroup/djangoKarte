# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-14 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metStanice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weatherstation',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]