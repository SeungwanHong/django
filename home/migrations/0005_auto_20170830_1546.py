# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 06:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20170830_1542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepost',
            old_name='phNo',
            new_name='phno',
        ),
        migrations.RenameField(
            model_name='homepost',
            old_name='pLaguage',
            new_name='planguage',
        ),
        migrations.RenameField(
            model_name='homepost',
            old_name='wExperience',
            new_name='wexperience',
        ),
    ]