# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 06:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepost_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepost',
            old_name='p_laguage',
            new_name='pLaguage',
        ),
        migrations.RenameField(
            model_name='homepost',
            old_name='ph_no',
            new_name='phNo',
        ),
        migrations.RenameField(
            model_name='homepost',
            old_name='w_experience',
            new_name='wExperience',
        ),
    ]